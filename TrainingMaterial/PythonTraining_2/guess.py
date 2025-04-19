max_val = 25
min_val = 1
tries = 0

print("Please enter h (too high), l (too low), or y (correct")
while True:
    guess = (max_val + min_val) // 2
#    answer = input("Is {0} your number? ".format(guess))
    answer = input("Is {0} your number {1}? " % (guess, "spam"))
    answer=answer.lower()
    if answer == "q":
        break

    tries += 1
    if answer == "h" or answer=="H":
        max_val = guess-1
    elif answer == "l":
        min_val = guess+1
    elif answer == "y":
        print("I got it in {0} try(ies)!".format(tries))
        break
    else:
        print("Please enter h (too high), l (too low), or y (correct")

