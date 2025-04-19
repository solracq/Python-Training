import math
import tkinter
import pyzmail

def basic():
    year_born = ('Paris Hilton', 1981)
    print(year_born)

    julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
    print(julia)

    print(julia[2])

    julia = julia[:3] + ("Shallow Hall", 2001) + julia[5:]
    print(julia)

    julia = julia[:3] + ("Sleeping with the enemy",) + julia[4:]
    print(julia)

    print(type(julia))

    (name, last_name, year_born, movie_title, movie_year, profession, b_place) = julia
    print(name)
    print(last_name)
    print(year_born)
    print(movie_title)
    print(movie_year)
    print(profession)
    print(b_place)

    # Assignment of values
    first = 'test'
    second = 'testarrosa'
    print(first, second)
    (first, second) = (second, first)
    print(first, second)

def f(r):
    # Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r**2
    return  (c, a)

def students():
    students = [
        ("John", ["CompSci", "Physics"]),
        ("Vusi", ["Maths", "CompSci", "Stats"]),
        ("Jessica", ["CompSci", "Accounting", "Economics", "Management"]),
        ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
        ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])
    ]

    for tuple_elem in students:
        print(tuple_elem[0])
        if type(tuple_elem[1]) == list:
            for i in range(len(tuple_elem[1])):
                print("\t",tuple_elem[1][i])
    print()

def julia_mo_inf():
    julia_more_info = (
        ("Julia", "Roberts"), (8, "October", 1967), "Actress", ("Atlanta", "Georgia"),
        [
            ("Duplicity", 2009),
            ("Notting Hill", 1999),
            ("Pretty Woman", 1990),
            ("Erin Brockovich", 2000),
            ("Eat Pray Love", 2010),
            ("Mona Lisa Smile", 2003),
            ("Oceans Twelve", 2004)
        ]
        )

    for elements in julia_more_info:
        if type(elements) == list:
            for movies in elements:
                print(movies)
        else:
            print(elements)

if __name__ == "__main__":
    basic()
    (circumference, area) = f(5)
    print('circumference =', circumference, " area =", area, "\n")
    students()
    julia_mo_inf()