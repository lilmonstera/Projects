from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

# Configure session to not use cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
db = SQL("sqlite:///Clubtomix.db")

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        phone = request.form.get("phone")
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if any fields are empty or invalid
        if not all([email, first_name, last_name, phone, username, password]):
            return ("all fields required")

        hash = generate_password_hash(password)

        # Insert new user information
        user_exists = db.execute(
                """INSERT INTO users (email, first_name, last_name, phone, username, hash) VALUES (?, ?, ?, ?, ?, ?) """,
                email, first_name, last_name, phone, username, hash
            )

        if not user_exists:
            return ("username or email already exists")

        return redirect("/login")

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":   # FIXED
        username = request.form.get("username")
        password = request.form.get("password")

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Validate login
        if len(user) != 1 or not check_password_hash(user[0]["hash"], password):
            return "Incorrect username or password"

        # Log user in
        session["user_id"] = user[0]["id"]

        return redirect("/dashboard")

    return render_template("login.html")

# Logout Page
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Dashboard Page
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    bookings = db.execute("""
    SELECT bookings.id, bookings.name, bookings.time, courses.name AS course_name
    FROM bookings
    JOIN courses ON bookings.course_id = courses.id
    WHERE bookings.user_id = ?
""", session["user_id"])

    courses = db.execute("SELECT * FROM courses")

    return render_template("dashboard.html", bookings=bookings, courses=courses)


# Book a course
@app.route("/book", methods=["POST"])
def book():
    if "user_id" not in session:
        return redirect("/login")

    name = request.form.get("name")
    time = request.form.get("time")
    course_id = request.form.get("course_id")
    email = request.form.get("email")
    number = request.form.get("number")

    if not name or not time or not course_id or not email:
        return "Please fill in missing information"

    db.execute(
        """
        INSERT INTO bookings (user_id, course_id, name, time, email, number)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        session["user_id"],
        course_id,
        name,
        time,
        email,
        number
    )

    return redirect("/dashboard")

    # Insert booking
    db.execute(
        "INSERT INTO bookings (user_id, course_id, name, time, email, number) VALUES (?, ?, ?, ?, ?, ?)",
        session["user_id"], course_id, name, time, email, number
    )

    return redirect("/dashboard")


# Cancel booking
@app.route("/cancel/<int:booking_id>")
def cancel(booking_id):
    if "user_id" not in session:
        return redirect("/login")

    db.execute(
        "DELETE FROM bookings WHERE id = ? AND user_id = ?",
        booking_id, session["user_id"]
    )

    return redirect("/dashboard")


# Run app
if __name__ == "__main__":
    app.run(debug=True)
