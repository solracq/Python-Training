name=("Doug", "George", "Alpana")
colors=("Green", "Blue", "Red")

# favColors=(("Doug", "Green"), ("George", "Blue"), ("Alpana", "Red"))
# favColors=zip(name, colors)

# for t in zip(name,colors):
#     print("{0}'s favorite color is {1}.".format(t[0], t[1]))
# 
# for (l, n,c) in zip(range(0, len(name)), name,colors):
#     print("{}: {}'s favorite color is {}.".format(l, n, c))

# for l, n in zip(range(0,len(name)), name):
#     print("{}: {}".format(l,n))

for l, n in enumerate(name):
    print("{}: {}".format(l,n))

          
# for n,c in favColors:
#     print("{0}'s favorite color is {1}.".format(n, c))
# 
# for (n,c) in favColors:
#     print("{0}".format(n))
# 
# [x,y]=[y,x]


