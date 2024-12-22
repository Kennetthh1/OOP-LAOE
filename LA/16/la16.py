class Appliances:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("OPERATING!!")
    
    def info(self):
        print(f"The {self.brand} is a model {self.model}")
class WasinghingMachine(Appliances):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliances):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliances):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Heating foods!")

lg =  WasinghingMachine("LG" , "WT2117NHB")
lg2 = Refrigerator("LG", "RVT-B093BS")
lg3 = Microwave("LG" , "25L NeoChef ™ Smart Inverter Microwave Oven")

for washingwashing in [lg, lg2, lg3]:
    washingwashing.operate()

lg.info()
lg2.info()
lg3.info()
