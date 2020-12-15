#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program checks to see if the number guessed is the random number


import random


def main():
    # this program checks to see if the number guessed is the random number
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # input, process & output
    while True:
        guessed_number = input("Enter a number(between 0-9): ")
        print("\n", end="")
        try:
            guessed_number = int(guessed_number)
            if guessed_number < 0 or guessed_number > 9:
                print("Please enter a number between 0-9")
                print("\n", end="")
            elif guessed_number > random_number:
                print("Number guessed was too high! Try a bit lower next time")
                print("\n", end="")
            elif guessed_number < random_number:
                print("Number guessed was too low. Guess a higher number.")
                print("\n", end="")
            else:
                print("Congratulations! You guessed the right number!")
                break
        except Exception:
            print("That was not a number. Please try again.")


if __name__ == "__main__":
    main()
