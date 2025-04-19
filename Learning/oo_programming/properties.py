# Python program to illustrate the use of @property decorator

class Properties:
    def __init__(self, lastname=None, firstname=None):
        self._lastname = lastname
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        if lastname is not None and not lastname.isalpha():
            raise ValueError("Last name may only contain letters")
        self._lastname = lastname

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        if firstname is not None and not firstname.isalpha():
            raise ValueError("First name may only contain letters")
        self._firstname = firstname


if __name__ == "__main__":
    p1 = Properties()
    p1.firstname = "Leo"
    p1.lastname = "Palm"
    print(f"{p1.firstname} {p1.lastname}")
    p2 = Properties("Curela", "Devil")
    print(f"{p2.firstname} {p2.lastname}")
    p3 = Properties("R2D2")
    print(f"{p3.firstname} {p3.lastname}")


