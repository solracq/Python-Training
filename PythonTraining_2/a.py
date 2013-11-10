import b

nih = b.nih

def nih(*args):
    print("Run away, run away...")

nih()
nih("Shrubbery")

def nih(*args):
    print("Something else")

nih("Swallow")

print (type(nih))
#b.spam("Shrubbery")

print(globals())
print("FromA " + __name__)
