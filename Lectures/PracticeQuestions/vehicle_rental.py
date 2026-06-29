class Vehicle:
    def __init__(self, regNo, rental_per_day):
        self.regNo = regNo
        self.rental_per_day = rental_per_day

    def display_info(self):
        print(f"Registration Number: {self.regNo}, Rental per Day: {self.rental_per_day}")
    def calculate_rental_cost(self, days):
        return self.rental_per_day * days

class Car(Vehicle):

    def __init__(self, regNo, rental_per_day, seating_capacity):
        super().__init__(regNo, rental_per_day)
        self.seating_capacity = seating_capacity
    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.seating_capacity}")

class Motorcycle(Vehicle):
    def __init__(self, regNo, rental_per_day, engine_capacity):
        super().__init__(regNo, rental_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}")

car1 = Car("Subaru-1234", 100, 5)
motorcycle1 = Motorcycle("Yamaha-5678", 50, 150)

car1.display_info()
print(f"Rental Cost for 3 days: {car1.calculate_rental_cost(3)}")

motorcycle1.display_info()
print(f"Rental Cost for 3 days: {motorcycle1.calculate_rental_cost(3)}")