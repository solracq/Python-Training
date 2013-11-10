#!/usr/bin/env python3

max_val = 26
min_val = 0
tries = 0

while True:
    guess = int((max_val + min_val)/2)
    answer = input("Is {0} your number? ".format(guess))

    if answer == "q":
        break

    tries = tries + 1

    if answer == "h":
        max_val = guess
    elif answer == "l":
        min_val = guess
    elif answer == "y":
        print("I got it in {0} try(ies)!".format(tries))
        break
    else:
        print("Please enter h, l, or y")

