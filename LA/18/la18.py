class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power= atk_power
   
    def basic_attack(self, target):
        target.health -= self.atk_power
        target.health = max(0, target.health)
        print(f"{self.name} attacked {target.name}. {target.name}'s health is now {target.health}.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount} points. {self.name}'s health is now {self.health}.")

Claude = Player("Claude", 1500, 50)  
Yz = Player("Yz", 2500, 80)  

while Claude.health > 0 and Yz.health > 0:
    Yz.basic_attack(Claude)
    if Claude.health > 0:
       Claude.basic_attack(Yz)

if Claude.health == 0:
   print(f"{Claude.name} has been defeated. {Yz.name} wins!")  

else:
   print(f"{Yz.name} has been defeated. {Claude.name} wins!")  
 
Claude.heal(100)   
