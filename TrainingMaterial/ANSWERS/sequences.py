#!/usr/bin/env python3

ctemps = [ -40.0, 0.0, 37.0, 75.0, 100.0 ]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

# ex 5-1
ftemps = [ c * 9 / 5 + 32 for c in ctemps]
for f,c in zip(ftemps,ctemps):
    print("{0:.1f} C is {1:.1f} F".format(c,f))

for c in ctemps:
    f = ((9 * c) / 5 ) + 32
    print("{0:.1f} C is {1:.1f} F".format(c,f))


# ex 5-2
clean_fruits = [ f.strip().lower() for f in fruits ]
fruitString=','.join(clean_fruits)
print(fruitString)

# ex 5-3
first = clean_fruits.pop(0)
clean_fruits.append(first)

rotated_fruits=clean_fruits[-1:]+clean_fruits[1:]

print(','.join(clean_fruits))


