#!/usr/bin/env python
# coding=utf-8
"""
Compete against the computer to see who can guess a number first
"""
import random
import time


def get_integer_input(msg: str) -> int:
    """
    Read user input until an integer is entered
    :param msg: the message to print to the user
    :return: the read in integer
    """
    while True:
        try:
            return int(input(msg + ': '))
        except ValueError:
            print("Input must be an integer")


if __name__ == '__main__':
    name = ''
    while not name:
        name = input('Please enter your name: ').strip()

    print("Hi {}, I'd like to challenge you to a number guessing game".format(name))
    time.sleep(0.5)
    print()

    # Get 2 integers from the user
    int1 = get_integer_input("Enter an integer for this little challenge")
    int2_prompt = "Thanks, now enter an integer that's different than the first one"
    while True:
        int2 = get_integer_input(int2_prompt)
        if int1 != int2:
            break
        int2_prompt = "Remember this integer needs to be different than the first one"

    # The cpu will use these numbers for its guessing range
    if int1 < int2:
        minimum = int1
        maximum = int2
    else:
        minimum = int2
        maximum = int1

    # Randomly select a number and start the guessing game
    answer = random.randint(minimum, maximum)
    print("\nOK, an integer in the range of {} and {} has been randomly chosen.\n"
          "Let's see who can guess it first.".format(minimum, maximum))

    while True:
        # Let the human guess and update the cpu's guessing range based on the results
        guess = get_integer_input("Enter your guess")
        if guess < answer:
            print("Too low")
            if guess >= minimum:
                minimum = guess + 1
        elif guess > answer:
            print("Too high")
            if guess <= maximum:
                maximum = guess - 1
        else:
            print("You got it!!")
            break

        # Let the computer guess and update its guessing range
        time.sleep(0.5)
        cpu_guess = (minimum + maximum) // 2

        if cpu_guess < answer:
            print("My guess of {} was too low".format(cpu_guess))
            minimum = cpu_guess + 1
        elif cpu_guess > answer:
            print("My guess of {} was too high".format(cpu_guess))
            maximum = cpu_guess - 1
        else:
            print("I guessed {} correctly!!".format(answer))
            break

        print()
