class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.year} {self.brand} {self.model} is driving.")

    def stop(self):
        if self.drive:
            print(f"The {self.year} {self.brand} {self.model} has stopped.")
        else:
            print(f"The {self.year} {self.brand} {self.model} is not driving.")

    __str__ = lambda self: f"{self.year} {self.brand} {self.model}"

car_brand = input("Enter the brand of the car: ")
car_model = input("Enter the model of the car: ")
car_year = int(input("Enter the year of the car: "))

car2 = Car(car_brand, car_model, car_year)

car2.drive()
car2.stop()
print(car2)