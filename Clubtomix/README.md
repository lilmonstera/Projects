# Clubtomix - Book golf your way
#### Video Demo:  [<https://youtu.be/CAdEf_sm9TE>]
#### Description: A "whole-in-one" app that helps you manage and keep track of your tee times without having to use multiple apps, why don't you book your tee time in one place.


# About Clubtomix
Clubtomix is built around the idea that booking golf should be effortless. Many golf courses still rely on outdated and admin communications systems, which can discourage new or younger players. Clubtomix addresses this by offering automate management system with a modern UI and a straightforward booking flow.

This project represents the foundation of a larger project. While the current version focuses on tee-time booking and management, the long-term goal is to expand Clubtomix to become Johannesburg's most used Golf booking app amongst golfers.

## Future Plans with Clubtomix
- Golf course memberships and subscription management
- Social features to see who you are playing with
- Ability to invite friends to join a booking
- Score tracking per round
- Handicap calculation and progress tracking

# Current Features
- User registration and authentication
- A simple Dashboard provided for logged-in users
- Keep track of booked tee times at featured golf courses
- Cancellation feature

# Design
Clubtomix was designed with the belief that golf can be modern, social and accessible to anyone at any age. And the beginning of that step is creating a tracker to help players keep track of their bookings and tee times.

The UI I created is to intentionally avoid messy and outdated booking systems typically found on course websites and focuses on the following:
- Clear Typography
- Responsive and touch friendly buttons
- Minimalistic and kind to the eye.

# Tech Stack
- Front-end: HTML & CSS
- Backend: Flask & Python
- Database: SQLite

# File Overview
## styles.css
This is my main formatting and styling for the design and overal UX and UI part of the app.
My main priorities when it came to design were the following:
- Minimalistic
- Modern
- Golf-themed
- Exclusivity

## dashboard.html
The main page after user login successful.

This page allows users to:
- View all their current tee-time bookings
- Cancel existing bookings
- Book new tee times using a form connected to the Clubtomix.db database

This is the core page of the application.

## index.html
This is the public landing page displayed before login and after logout.

It introduces users to Clubtomix, introduces the users to the purpose of the app, and encourages registration or login.

## layout.html
This is the base html template that sets up other html pages with reciporical sttructure, styles and blocks. To avoid duplication, errors and keeping a consistent structure.

It contains:
- Navigation structure
- Global styles and assets
- Jinja template blocks used by other pages

## login.html
- Handles user authentication
- Users can enter their unique username and password
- Form validation (Unique passwords)

## register.html
- Provides a path for a potential player to become a user
- User credentials are entered in.

## app.py
The main application file that gets the file to run by connecting the frontend templates with backend logic as well as the database.

It contains the following:
- Route definitions
- Databse queries
- Booking process/logic
- User Validation logic
- Sessions

## Clubtomix.db
This is the database that holds all raw data from the application.

It stores the following:
- Users information
- Golf courses
- Bookings

### Copyright and Use of AI:
All images used were from Pinterest and are not to be used for public use but just for aesthetics and as protptypes

AI was used for the testing and adding blur to the navigation as well as the hero section but it was not used for the rest of this project
