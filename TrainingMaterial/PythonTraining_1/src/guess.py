'''
Created on Sep 25, 2013

@author: cquiroz
'''

if __name__ == '__main__':
    pass

max_val = 26
min_val = 0
tries = 0

print("Think of a number and I wil guss it, Enter \"l\" if too low, \"h\" if too high, or \"y\" if I got it ")

while True:
    guess = (max_val + min_val) // 2 # automatically the "//" rounds down
    usr = input("Is your number is {0}? ".format(guess))
    usr = usr.lower()

    if usr == "q":
        break

    tries += 1

    if usr == "h" or usr == "H" :
        max_val = guess - 1
    elif usr == "l" or usr =="L" :
        min_val = guess + 1
    elif usr == "y" or usr == "Y" :
        print("I got the answer right! at the {0} tries".format(tries))  
        break
    else :
        print("Enter \"l\" if too low, \"h\" if too high, or \"y\" if I got it") 
