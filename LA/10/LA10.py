print("LA#3")

class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
        print(f"{self.brand} has {self.model} with {self.fuel_type}")

class Motorcyle(Vehicle):
     pass

vehicle = Motorcyle("Kawasaki", "ZR1000" , "Gasoline")
vehicle.describeVehicle()

class Cars(Vehicle):
     pass
vehicle1 = Cars("Honda", "FD" , "Gasoline")
vehicle1.describeVehicle()
