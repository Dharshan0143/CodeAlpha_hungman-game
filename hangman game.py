import random

# List of words and their corresponding clues
word_list = [
    {'word': 'python', 'clue': 'A popular programming language'},
    {'word': 'hangman', 'clue': 'A classic word guessing game'},
    {'word': 'programming', 'clue': 'The process of writing computer software'},
    {'word': 'openai', 'clue': 'The AI research lab behind ChatGPT'},
    {'word': 'gpt', 'clue': 'A type of AI language model'},
    {'word': 'chatbot', 'clue': 'A program designed to simulate conversation'},
    {'word': 'computer', 'clue': 'An electronic device for storing and processing data'}
]

# Simple hangman stages (text-based "animation")
hangman_stages = [
    """
    -----
    |   |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |   |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  /
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    |
    --------
    """
]

def choose_word(word_list):
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_single_round(selected):
    word = selected['word']
    clue = selected['clue']
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = len(hangman_stages) - 1

    print(f"\nClue: {clue}")

    while incorrect_guesses < max_incorrect_guesses:
        current_state = display_current_state(word, guessed_letters)
        print(hangman_stages[incorrect_guesses])
        print("\nWord:", current_state)
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            guessed_letters.add(guess)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            return True

    print(hangman_stages[incorrect_guesses])
    print("\nSorry, you've run out of guesses. The word was:", word)
    return False

def hangman():
    print("Welcome to Hangman!")
    print("You need to guess the word by guessing one letter at a time.")
    print("Let's start the game!\n")

    while True:
        selected = choose_word(word_list)
        play_single_round(selected)
        
        # Ask the player if they want to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    hangman()
