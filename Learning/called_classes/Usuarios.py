class Usuarios():
    def __init__(self, first_name, last_name, affiliaton, id, fav_zodiac_knight):
        self.first_name = first_name
        self.last_name = last_name
        self.affiliaton = affiliaton
        self.id = id
        self.fav_zodiac_knight = fav_zodiac_knight
        self.login_attempts = 0

    def describe_user(self):
        dictionary = dict()
        dictionary["first_name"] = self.first_name
        dictionary["last_name"] = self.last_name
        dictionary["affiliaton"] = self.affiliaton
        dictionary["id"] = self.id
        dictionary["fav_zodiac_knight"] = self.fav_zodiac_knight
        dictionary["login_attempts"] = self.login_attempts
        for key, value in dictionary.items():
            print(f"{key} : {value}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, who likes '{self.fav_zodiac_knight}'")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

###########################################################################
class Admin(Usuarios):
    """Child class that inherits form 'Usuarios' class."""
    def __init__(self, first_name, last_name, affiliaton, id, fav_zodiac_knight):
        super().__init__(first_name, last_name, affiliaton, id, fav_zodiac_knight)
        # self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add admin rights']
        self.privileges = Privileges()

    # def show_privileges(self):
    #     print(f"Usuario {self.first_name} {self.last_name} has Admin rights so the following actions can be performed: {self.privileges}")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Privileges():
    """A class that can be used with the class Admin to store and show user Admin's privileges."""
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user', 'can add admin rights']):
        self.privileges = privileges

    def show_privileges(self):
        print(f"User has Admin rights so the following actions can be performed: {self.privileges}")

#--------------------------------------------------------------------------
if __name__ == "__main__":
    user1 = Usuarios("Chanel", "Keui", "Republican", 123456, "Mu Aries")
    user2 = Usuarios("Stewie", "Q", "Democrat", 654321, "Ikki")
    user3 = Usuarios("Norman", "K", "Democarat", 9684500, "Saori Kido")
    user1.describe_user()
    user2.describe_user()
    user3.describe_user()
    user1.greet_user()
    user2.greet_user()
    user3.greet_user()
    for i in range(7):
        user1.increment_login_attempts()
    user1.describe_user()
    user1.reset_login_attempts()
    user1.describe_user()
    print()

    admin_user = Admin("Dn Lalo", "Qui", "PRI", 190854309, "Shura de Capricornio")
    admin_user.describe_user()
    # admin_user.show_privileges()
    admin_user.privileges.show_privileges()
    admin_user.privileges.privileges = ['modify system', 'delete system']
    admin_user.privileges.show_privileges()