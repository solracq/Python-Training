from animal import Animal

class Mammal(Animal):
    '''
        An animal that gives birth tolive offspring (as opposed to laying eggs).
    '''
    def __init__(self, species, name, sound, gestation):
        super().__init__(species, name, sound)
        self._gestation = gestation

    @property
    def gestation(self):
        """Length of gestation period in days"""
        return self._gestation

if __name__ == "__main__":
    m1 = Mammal("African lion", "Simba", "Roarrrr", 120)
    print(f"{m1.name} is a {Mammal.tformat(m1.species)} -- {m1.make_sound()}")
    print(f"Number of animals {Mammal.zoo_size()}")
    m2 = Mammal("Fruit bat", "Freddie", "Squeak!!", 180)
    print(f"{m2.name} is a {Mammal.tformat(m2.species)} -- {m2.make_sound()}")
    print(f"Number of animals {Mammal.zoo_size()}")
    print(f"Number of animals {m2.zoo_size()}")
    m1.kill()
    print(f"Number of animals {Mammal.zoo_size()}")
    zoo_animals = [m1, m2]
    for animal in zoo_animals:
        print(f"Gestation period of the {animal.species} is {animal.gestation} days")

