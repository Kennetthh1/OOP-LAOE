class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

kotse1 = Car("Civic", "Gray")
print(kotse1.brand, kotse1.color)

kotse2 = Car("BMW", "Black")
print(kotse2.brand, kotse2.color)

kotse1.color = "Pink"
print(kotse1.brand, kotse2.color)

kotse2.color = "Neon Green"
print(kotse2.brand, kotse2.color)
