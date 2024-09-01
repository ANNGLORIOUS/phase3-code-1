class Car:
    """The _init__ method  sets the make,model and year of the car."""
    def __init__(self, make, model, year):
        """The self keyword refers to the instance of the car class."""
        self.make = make  
        self.model = model
        self.year = year

    def display_info(self):
        """Display information about the car"""
        return f"{self.make} {self.model} ({self.year})"

my_car = Car("Honda", "CRV", 2019)
print(my_car.display_info())
