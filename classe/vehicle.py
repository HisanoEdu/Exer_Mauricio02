
class Vehicle:
    def __init__(self, brand, model): 
        self.brand = brand # marca 
        self.model = model # modelo

    def fuel_type(self):
        return "Unknown" # desconhecido

    def passenger_capacity(self):
        return 0

class Car(Vehicle):
    def fuel_type(self):
        return "Gasoline"

    def passenger_capacity(self):
        return 5

class Motorcycle(Vehicle): # moto
    def fuel_type(self):
        return "Gasoline"

    def passenger_capacity(self):
        return 2

class Truck(Vehicle): #caminhão
    def fuel_type(self):
        return "Diesel"

    def passenger_capacity(self):
        return 2

def demonstrate_vehicles():
    vehicles = [
        Car("Toyota", "Corolla"),
        Motorcycle("Honda", "CB500"),
        Truck("Volvo", "FH540")
    ]

    for vehicle in vehicles:
        print("Brand: " + vehicle.brand)
        print("Model: " + vehicle.model)
        print("Fuel Type: " + vehicle.fuel_type())
        print("Passenger Capacity: " + str(vehicle.passenger_capacity()))
        
demonstrate_vehicles()

