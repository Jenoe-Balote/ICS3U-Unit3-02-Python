#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program is the "Number Guessing Game"


import constant


def main():
    # this function runs the "Number Guessing Game"

    # input
    number_guessed = int(input('Enter a number between 0 - 9: '))
    print("")

    # process and output
    if number_guessed == 5:
        print("Correct!")
    if number_guessed != 5:
        print("Incorrect!")


if __name__ == "__main__":
    main()
