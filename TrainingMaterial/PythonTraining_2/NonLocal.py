var = 0
def outer():
    var = 1
    def inner():
#       global var
        var = 2
        print('inner:', var)
    inner()
    print('outer:', var)
outer()
print('main:', var)
