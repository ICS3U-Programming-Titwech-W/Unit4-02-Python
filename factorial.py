#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Titwech Wal
# Modified on: Apirl 22, 2021
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    factorial_answer = 1

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")

    try:
        # convert to string
        user_number = int(user_number_string)
        # if number input is positive
        if user_number >= 0:
            # calculate the sum of all numbers from 0 to num input
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                if loop_counter >= user_number:
                    break
            print("")
            print("{}! = {}".format(user_number, factorial_answer))

        else:
            print('You entered a negitive number, try again')

    except Exception:
        print("{} is not a valid number.". format(user_number_string))


if __name__ == "__main__":
    main()
