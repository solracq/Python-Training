class Dog():
    """A Simple attempt to model a dog."""

    # Constructor
    def __init__(self, name, age):
        """Initializing name and age attributes."""
        self.name = name
        self.age = age

    def set_name(self, name):
        """Set a new name for the dog"""
        self.name = name

    def get_name(self):
        """Get dog's name"""
        return self.name
    
    def set_age(self, age):
        """Set a new age for the dog"""
        self.age = age

    def get_age(self):
        """Get dog's age"""
        return self.age
    
    def sit(self):
        """Simulate a dog sitting in response to command."""
        print(self.name.title() + " is now sitting.")

    def rollover(self):
        """Simulate rollover in response to command"""
        print(self.name.title() + " rolled over!")

if __name__ == "__main__":
    dog = Dog('koko', 5)
    print(dog.name)
    print(dog.age)
    dog.set_name("cloi")
    dog.set_age(3)
    print(dog.get_name())
    print(dog.get_age())
    dog.sit()
    dog.rollover()