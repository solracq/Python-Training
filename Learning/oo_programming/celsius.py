# Python program to illustrate the use of @property decorator

class Celsius:
    def __init__(self, temp=0):
        self._temp = temp

    @property
    def temp(self): # Getter method
        return f"The value of the temperature is: {self._temp}"

    @temp.setter
    def temp(self, value): # Setter method
        if value < -273:
            raise ValueError("It is a vlue error.")
        self._temp = value

    @temp.deleter
    def temp(self): # Deleter method
        del self._temp


if __name__ == "__main__":
    celcius = Celsius()
    celcius.temp = 270
    print(celcius.temp)
    celcius.temp = -300
    print(celcius.temp)
