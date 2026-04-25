class BMW:
    def fuel_type(self):
        print("BMW uses Petrol.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses High-octane Petrol.")

def check_fuel(car):
    car.fuel_type()

car1 = BMW()
car2 = Ferrari()

check_fuel(car1)
check_fuel(car2)