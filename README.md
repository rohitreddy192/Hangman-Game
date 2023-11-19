# Hangman - Multiplayer Word-Guessing Game
  This Python program implements a multiplayer word-guessing game where two players take turns entering words for the other player to guess. The game keeps track of scores for both players and allows players to exit the game at any time.

## How to Play:
### Run the Python script: 
    multiplayer_game.py
  
  - Player 1 enters a word for Player 2 to guess or types 'exit' to end the game.
  - Player 2 guesses the characters of the word entered by Player 1.
  - Players take turns entering words and guessing until one of them types 'exit'.

## Code Documentation:
  The Python code includes two functions:

  1. **guess_word(word_to_guess, max_turns=12):** Manages the guessing phase of the game, checking guesses and updating the game state.
  2. **multiplayer_game():** Orchestrates the multiplayer game, alternating between players for word entry and guessing.

## Additional Information:
  1. The game masks the word being entered by one player to ensure secrecy while the other player guesses.
  2. Scores are displayed after each round and final scores are shown at the end of the game.
