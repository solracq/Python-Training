class Animal:
    count = 0
    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal.count += 1

    def kill(self):
        Animal.count -= 1

    @property # To specify a Getter method
    def species(self):
        return self._species

    @property # To specify a Getter method
    def name(self):
        return self._name

    def make_sound(self):
        return self._sound

    @staticmethod
    def tformat(string:str):
        return string.title()

    @classmethod
    def zoo_size(cls):
        return cls.count

if __name__ == "__main__":
    leo = Animal("African Lion", "Leo", "Roarrrrrr")
    garfield = Animal("cat", "Garfield", "Meowwwww")
    felix = Animal("cat", "Felix", "Meowwwww")

    print(f"{leo.name} is a {Animal.tformat(leo.species)} -- {leo.make_sound()}")
    print(f"{garfield.name} is a {Animal.tformat(garfield.species)} -- {garfield.make_sound()}")
    print(f"{felix.name} is a {Animal.tformat(felix.species)} -- {felix.make_sound()}")
    print(f"The size of the Zoo is {Animal.zoo_size()}")