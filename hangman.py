import random

words = ["PYTHON", "PROGRAMMING", "COMPUTER", "SCIENCE", "ALGORITHM", "DATA", "STRUCTURE", "FUNCTION", "VARIABLE", "DICTIONARY", "LIST", "LOOP", "CLASS", "OBJECT", "INHERITANCE", "POLYMORPHISM", "ENCAPSULATION", "ABSTRACTION"]

def get_word():
    word = random.choice(words)
    return word

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print()
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if guess in guessed_letters or guess in guessed_words:
            print("You already guessed", guess)
        elif len(guess) == 1 and guess.isalpha():
            if guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            tries -= 1
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
        ---------
        """,
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
        ---------
        """,
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
        ---------
        """,
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
        ---------
        """,
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
        ---------
        """,
        """
            --------
            |      |
            |      O
            |      
            |      
            |
        ---------
        """
    ]
    return stages[tries-1]

if __name__ == "__main__":
    word = get_word()
    play(word)
    while input("Want to play again [y or n]: ").lower() == "y":
        play(word)