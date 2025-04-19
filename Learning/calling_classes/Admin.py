# from Learning.called_classes.Users import Users
# from Learning.called_classes.Privileges import Privileges

from car import Car, ElectricCar, CarBattery

# class Admin(Users):
#     def __init__(self, first_name, last_name, age, hobby):
#         super().__init__(first_name, last_name, age, hobby)
#         self.privileges = Privileges()

# print()
# admin = Admin("Nm", "Q.", 5, "Drawing")
# admin.create_records()
# admin.print_records()
# admin.privileges.show_privileges()

my_car = Car("Nissan", "Versa", "2007")
my_car.get_description()