import random

correct = 'you guessed correctly!'
too_low = 'too low!!'
too_high = 'too high!'
guesses = []


# Set the high and low values for the random number
def configure_range():
    try:
        low_num = int(input("What is the lower number? "))
        high_num = int(input("What is the higher number? "))
        return (low_num, high_num)
    except Exception:
        print("Something went wrong. Please re-enter your desired integers.")


# Generate a secret number for the user to guess
def generate_secret(low, high):
    return random.randint(low, high)


# Get user's guess
def get_guess():
    guess = 0
    try:
        guess = int(input("Guess the secret number: "))
    except Exception:
        print("That isn't an integer, please try again.")
    return guess


# Compare guess and secret, return string describing result of comparison
def check_guess(guess, secret):
    if guess == secret:
        guesses.append("1")
        print("Total number of guesses: " + str(len(guesses)))
        return correct
    if guess < secret:
        guesses.append("1")
        print("Guess #" + str(len(guesses)))
        return too_low
    if guess > secret:
        guesses.append("1")
        print("Guess #" + str(len(guesses)))
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break



if __name__ == '__main__':
    while True:
        main()
        play_again = input('Do you want to play again? Y/N  ')
        if play_again != "y":
            break
