"""A class that can be used to represent a car."""

class Car():
    """A simple attempt to represet a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    @classmethod
    def change_view_format():
        pass

    @staticmethod  #It doesn't need to be called through an instance but through the class. 
    #It is used to implement configurable behaivour, or to organize a bundle of methods.
    def car_properties():
        pass

    def get_descriptive_name(self):
        """Retrun a neatly formated descriptive name."""
        msg = str(self.year) + " " + self.make + " " + self.model
        return msg.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car as {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attepts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer...only Matilda's father can do that!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"Filling gas tank of {self.make} - {self.model}...")

###############################################################################
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make,model, year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     """print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("Electric cars don't have gas tanks.")

    def parent_gas_tank(self):
        return super().fill_gas_tank()
#-----------------------------------------------------------------------
class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """print a statement about the range this battery provide"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print(f"Battery size has been upgraded to {self.battery_size}")
        elif self.battery_size == 85:
            print(f"Battery of size {self.battery_size} doesn't need upgrade")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

if __name__ == "__main__":
    my_new_car = Car('audi', 'a4', 2007)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    my_new_car.update_odometer(55)
    my_new_car.read_odometer()
    my_new_car.update_odometer(12)
    my_new_car.increment_odometer(12)
    my_new_car.read_odometer()
    my_new_car.fill_gas_tank()
    print()

    my_electric_car = ElectricCar('bmw', 'x9', 2018)
    print(my_electric_car.get_descriptive_name())
    # my_electric_car.describe_battery()
    my_electric_car.fill_gas_tank()
    my_electric_car.battery.describe_battery()
    my_electric_car.battery.get_range()
    my_electric_car.battery.upgrade_battery()
    my_electric_car.battery.get_range()
    my_electric_car.battery.upgrade_battery()
    my_electric_car.parent_gas_tank()