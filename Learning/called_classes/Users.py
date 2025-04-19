# A class to record User info
class Users():
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.dict_user = {}
        self.login_attempts = 0

    def set_full_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

    def set_hobby(self, hobby):
        self.hobby = hobby

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return self.age

    def get_hobby(self):
        return self.hobby

    def create_records(self):
        self.dict_user = {'first_name': self.first_name, 'second_name': self.last_name,
                          'age': self.age, 'hobby': self.hobby}
        return self.dict_user

    def print_records(self):
        for key, value in sorted(self.dict_user.items()):
            print(f"{key}:{value}")

    def greet_user(self):
        question = f"Hello {self.get_full_name()}, would you like {self.hobby}?"
        answer = input(question)
        if answer == 'yes' or answer == "y":
            print("Great, lets {}".format(self.hobby))
        else:
            print("It's OK we can read books then!")

    def get_future_age(self):
        print(f"{self.first_name}, next year you will be, {self.age + 1} ")

    def print_login_attempts(self):
        print(f"login attempts = {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = Users('Pete', 'Q.', 7, 'playing lego Mario')
user1.get_full_name()
user1.create_records()
user1.print_records()
user1.greet_user()
user1.get_future_age()
user1.print_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.print_login_attempts()
user1.reset_login_attempts()
user1.print_login_attempts()