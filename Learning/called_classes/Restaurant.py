class Restaurant():
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def set_restaurant_name(self, restaurant_name):
        self.restaurant_name = restaurant_name

    def set_cusine_type(self, cusine_type):
        self.cusine_type = cusine_type

    def get_restaurant_name(self):
        return self.restaurant_name
    
    def get_cusine_type(self):
        return self.cusine_type
    
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name}' serves '{self.cusine_type}'. It has served {self.number_served} customers")

    def open_restaurant(self):
        print(f"Restaurant '{self.restaurant_name}' is OPEN!")

    def set_number_served(self, customer_served):
        self.number_served = customer_served

    def increment_number_served(self, customer_served):
        if customer_served > self.number_served:
            self.number_served += customer_served
        else:
            print("The number of customers served cannot be decremented")

##################################################################
class IceCreamStand(Restaurant):
    """IceCreamStand type of restaurant that inherits from the Restaurant parent class"""
    def __init__(self, restaurant_name, cusine_type):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = ['strawberry', 'chocolate', 'vanilla']

    def available_flavors(self):
        print(f"Welcome to the Restaurant '{self.restaurant_name}' of '{self.cusine_type}'. We have the following icream flavors: {self.flavors}")

if __name__ == "__main__":
    my_restaurant = Restaurant("Bajo el cielo de Jalisco", "Mexican Cusine")
    print(my_restaurant.get_restaurant_name())
    print(my_restaurant.get_cusine_type())
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    my_restaurant.set_restaurant_name("Munich")
    my_restaurant.set_cusine_type("German Cusine")
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    my_restaurant.number_served = 9
    my_restaurant.describe_restaurant()
    my_restaurant.set_number_served(18)
    my_restaurant.describe_restaurant()
    my_restaurant.increment_number_served(5)
    my_restaurant.increment_number_served(38)
    my_restaurant.describe_restaurant()

    my_icecream_stand = IceCreamStand("Gellato", "Italian Icream Cousine")
    my_icecream_stand.describe_restaurant()
    my_icecream_stand.available_flavors()