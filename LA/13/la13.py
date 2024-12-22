class Animals():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def describeCar(self):
        print(f"{self.name} with {self.price} price")

class Fish(Animals):
    def __init__(self, name, price, can_swim):
        super().__init__(name, price)
        self.can_swim = can_swim

pesh = Fish("talapya","na lumalangoy", True)
print(pesh.can_swim)
