from enum import Enum

class Seassons(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

if __name__ == "__main__":
    print(Seassons.SPRING.name)
    print(Seassons.WINTER.value)
    print()
    print(Seassons["AUTUMN"])
    print(Seassons["AUTUMN"].name)
    print(Seassons["AUTUMN"].value)
    print()
    print(Seassons(2))
    print(Seassons(2).name)
    print(Seassons(2).value)
    print()
    print(type(Seassons.SPRING))
    print(repr(Seassons.SPRING))
    print(list(Seassons))

    # Hashing the enum
    dictionary = {}
    dictionary[Seassons.SPRING.name] = 'Prmavera'
    dictionary[Seassons.SUMMER.name] = 'Verano'
    print(dictionary)

    for seasson in Seassons:
        print(f"{seasson.name}: {seasson.value}")
