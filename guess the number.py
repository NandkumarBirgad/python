def guess_number():
    number_to_guess = 100
    guess = 1

    print("Guess the number (between 1 and 100):")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))

        if guess > 78:
            print("Guess is too large!  stop the game.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
guess_number()            


