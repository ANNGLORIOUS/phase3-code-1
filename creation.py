class Car:
    def __init__(self, make, model, year):
        self.make = make  
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.make} {self.model} ({self.year})"

my_car = Car("Honda", "CRV", 2019)
print(my_car.display_info())
