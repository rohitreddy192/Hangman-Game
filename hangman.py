import getpass

def guess_word(word_to_guess, max_turns=12):
    word = word_to_guess.lower()
    hidden_word = ['_' for _ in word]
    guesses = ''
    turns = max_turns

    while turns >= 0:
        print(" ".join(hidden_word))

        if '_' not in hidden_word:
            print("\nYou Win!")
            print("The word is:", word_to_guess)
            break

        print()
        guess = input("Guess a character: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guesses:
            print("You already guessed that character. Try a different one.")
            continue

        guesses += guess
        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    hidden_word[i] = guess
        else:
            turns -= 1
            print("Wrong guess!")
            print("You have", turns, 'guesses left')

            if turns == 0:
                print("You Lose! The word was:", word_to_guess)
                break
        if ''.join(hidden_word) == word_to_guess: return True
    return ''.join(hidden_word) == word_to_guess

def multiplayer_game():
    player1_score = 0
    player2_score = 0
    turn = 1

    while True:
        if turn % 2 != 0:
            print("\nPlayer 1's turn:")
            player1_word = getpass.getpass("Player 1, please enter a word for Player 2 to guess (type 'exit' to end the game): ")
            if player1_word.lower() == 'exit':
                break
            print("\nPlayer 2, start guessing!")
            result = guess_word(player1_word, max_turns=len(player1_word)*2)
            if not result:
                player1_score += 1
            else:
                player2_score += 1
        else:
            print("\nPlayer 2's turn:")
            player2_word = getpass.getpass("Player 2, please enter a word for Player 1 to guess (type 'exit' to end the game): ")
            if player2_word.lower() == 'exit':
                break
            print("\nPlayer 1, start guessing!")
            result = guess_word(player2_word, max_turns=len(player2_word)*2)
            if not result:
                player2_score += 1
            else:
                player1_score += 1

        print("\nCurrent Scores:")
        print(f"Player 1: {player1_score}  Player 2: {player2_score}")
        turn += 1

    print("\nFinal Scores:")
    print(f"Player 1: {player1_score}  Player 2: {player2_score}")

multiplayer_game()