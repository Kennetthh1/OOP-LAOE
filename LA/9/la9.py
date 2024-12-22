class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"
kotseuno = Car("Lambo")
print(kotseuno)

del kotseuno
#print(car1)
