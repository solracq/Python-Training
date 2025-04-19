#!/usr/bin/env python3

while True:
    name = input("Enter a name (or q to quit): ")
    if name.lower().startswith("q"):
        print("goodbye!")
        break
    print("welcome, ",name)
