# Program to demonstrate the use of the @property decorator

class Portal:
    def __init__(self):
        self._name = ""

    @property # Specifying a "getter" method
    def name(self):
        return self._name

    @name.setter # Using the same method name as in the @property with "setter", makes the method a setter method.
    def name(self, value):
        self._name = value

    @name.deleter # Using the same method name as in the @property with "deleter", makes the method a deleter method.
    def name(self):
        del self._name

if __name__ == "__main__":
    portal = Portal()
    portal.name = "Calo" # Setting name
    print(portal.name) # Printing name
    del portal.name # Deleting name
    print(portal.name)