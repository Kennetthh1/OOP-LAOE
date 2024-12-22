class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Bark!")

class Cat:
   def __init__(self, name):
       self.name = name
   def speak(self):
        print("Meow!")

class Bird:
   def __init__(self, name):
       self.name = name
   def speak(self):
        print("Chirp!")

class Fish:
    def __init__(self, name):
       self.name = name
    def speak(self):
        print("....")


doggy = Dog("Doggy")
meow = Cat("Muning")
birdie = Bird("mayang mababa ang lipad")
talapya = Fish("Talapyang adobo")

def animal_sounds(animal):
    animal.speak()

for nimal in [doggy, meow, birdie, talapya]:
    animal_sounds(nimal)

