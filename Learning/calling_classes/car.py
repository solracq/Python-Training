"""A class that can be used to represent a car."""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        print(f"{self.make}, {self.model},  {self.year}")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it!")

    def update_odometer(self, millage):
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("You cannot roll back an odometer")

    def increase_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling tank...")

class CarBattery:
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery size of this car is: {self.battery_size}KWh battery")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = CarBattery()

    def fill_gas_tank(self):
        print("This CAr doesn't need a gas tank!")

    def get_battery_range(self):
        print(f"Battery range: 0-{self.battery.battery_size}")


# my_versa = Car("Nissan", "Versa", "2007")
# my_versa.get_description()
# my_versa.increase_odometer(50)
# my_versa.update_odometer(10)
# my_versa.update_odometer(60)
# my_versa.read_odometer()
# my_versa.fill_gas_tank()
# print()
# my_tesla = ElectricCar("Tesla", "model Y", "2023")
# my_tesla.get_description()
# my_tesla.increase_odometer(10)
# my_tesla.read_odometer()
# my_tesla.fill_gas_tank()
# my_tesla.get_battery_range()
# my_tesla.battery.describe_battery()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.get_battery_range()