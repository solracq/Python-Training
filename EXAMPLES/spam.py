#!/usr/bin/env python3

# Module Spam -- provides a tasty breakfast

# separator for toast toppings
topsep = " and "

def eggs(how):
    "cook some eggs"
    print("Cooking up some lovely {0} eggs".format(how))

def toast(*toppings):
    """cook some toast
            -- add dairy products
            -- add fruity spreads """
    print("Toasting up some toast with ",topsep.join(toppings))


