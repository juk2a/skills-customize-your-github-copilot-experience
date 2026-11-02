# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game to practice Python strings, loops, conditionals, random selection, and user input. The game should let a player guess a hidden word one letter at a time before they run out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word from the provided list and initialize the variables needed to track the player's guesses and remaining attempts.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Track the letters the player has guessed.
- Set and track a maximum of 6 incorrect guesses.

### 🛠️ Play a Round of Hangman

#### Description
Create a loop that shows the player's progress, asks for a letter, and updates the game until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Display each letter in the secret word as a letter if guessed or an underscore if not guessed (for example, `_ _ _`).
- Ask the player to enter a letter and check whether it appears in the secret word.
- Update the guessed letters after each turn and reduce the remaining attempts for an incorrect guess.
- End when the player has guessed the word or used all 6 incorrect guesses.
- Display a clear win or loss message; when the player loses, reveal the secret word.
