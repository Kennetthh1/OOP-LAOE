class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def describeCar(self):
        print(f"{self.name} with {self.price} price")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

hatwils = Car("Hatwils2k24","200M")
hatwils.describeCar()
