#!/usr/bin/env python3

states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt","w") as statefile:
    for state in states:
        statefile.write(state + "\n")
