import random

def playAgain():
    playAgain = input("Do you want to play again? (yes/no): ")
    if playAgain.lower() == "yes":
        playHangman()

def playHangman():
    words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange", "pear", "quince", "strawberry", "tangerine", "watermelon"]
    word = random.choice(words).lower()
    guessedLetters = []
    attempts = 6

    while True:
        print("\nTries left: ", attempts)
        hiddenWord = ""
        for char in word:
            if char in guessedLetters:
                hiddenWord += char
            else:
                hiddenWord += "_"

        print("Word: ", hiddenWord)

        if hiddenWord == word:
            print("Congratulations, you guessed the word!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessedLetters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Correct!")
            guessedLetters.append(guess)
        else:
            print("Incorrect.")
            attempts -= 1
            guessedLetters.append(guess)

        if attempts == 0:
            print("Game over! The word was:", word)
            break

    playAgain()

print("Welcome to Hangman!")
playHangman()
