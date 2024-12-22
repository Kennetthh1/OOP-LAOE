from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name ):
        super().__init__()
        self.name = name 
    @abstractmethod
    def attack(self):
        pass 
class Warrior(GameCharacter):
    def attack(self):
        print(f"Swings sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an Arrow!!")
class Healer(GameCharacter):
    def attack(self):
        print("Casts healing spell on ally!")


war = Warrior("Arlott") 
mag = Mage("alice")
ewan = Archer("Miya")
db1 = Healer("EWAN KO NA")

war.attack()
mag.attack()
ewan.attack()
db1.attack()
