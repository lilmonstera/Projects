function getTodayKey() {
  const now = new Date();
  return `${now.getFullYear()}-${now.getMonth() + 1}-${now.getDate()}`;
}

function getDayOfYear(date) {
  const start = new Date(date.getFullYear(), 0, 0);
  const diff = date - start;
  return Math.floor(diff / (1000 * 60 * 60 * 24));
}

const promptScreen = document.getElementById("prompt-screen");
const affirmationScreen = document.getElementById("affirmation-screen");
const promptText = document.getElementById("prompt-text");
const journalInput = document.getElementById("journal-input");
const affirmationText = document.getElementById("affirmation-text");
const completeBtn = document.getElementById("complete-btn");
const skipBtn = document.getElementById("skip-btn");
const doneBtn = document.getElementById("done-btn");

const todayKey = getTodayKey();
const journalStorageKey = `journal-${todayKey}`;

// Daily prompt rotation: same prompt all day, changes automatically tomorrow.
const dayOfYear = getDayOfYear(new Date());
const todaysPrompt = PROMPTS[dayOfYear % PROMPTS.length];
promptText.textContent = todaysPrompt;

// Restore any in-progress entry from earlier today.
const savedEntry = localStorage.getItem(journalStorageKey);
if (savedEntry) {
  journalInput.value = savedEntry;
}

journalInput.addEventListener("input", () => {
  localStorage.setItem(journalStorageKey, journalInput.value);
});

function showAffirmation() {
  const affirmation =
    AFFIRMATIONS[Math.floor(Math.random() * AFFIRMATIONS.length)];
  affirmationText.textContent = affirmation;
  promptScreen.classList.add("hidden");
  affirmationScreen.classList.remove("hidden");
}

completeBtn.addEventListener("click", showAffirmation);
skipBtn.addEventListener("click", showAffirmation);

doneBtn.addEventListener("click", () => {
  affirmationScreen.innerHTML = `
    <p class="eyebrow">Until tomorrow</p>
    <p class="closing-message">Take care of yourself. A new reflection will be waiting for you tomorrow.</p>
  `;
});
