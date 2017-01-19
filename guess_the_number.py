import random

correct = 'you guessed correctly!'

too_low = 'too low!!'
too_high = 'too high!'
guesses = []


def configure_range():
    # Set the high and low values for the random number

    return 1, 20


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    guess = 0
    try:
        guess = int(input("Guess the secret number: "))
    except Exception:
        print("That isn't an integer, please try again.")
    return guess


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        guesses.append("1")
        print("Total number of guesses: " + str(len(guesses)))
        return correct
    if guess < secret:
        guesses.append("1")
        print("Guess #" + str(len(guesses)))
        return too_low
    if guess > secret:
        print("Guess #" + str(len(guesses)))
        guesses.append("1")
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
    main()
