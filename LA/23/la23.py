class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name 
        self.ability = ability
    def introduce(self, func):
        def kupal(*args, **kwargs):
            print("Introducing.............")
            func(*args, **kwargs)
            print("This character is awesome!!!")
        return kupal

naruto = AnimeCharacter("Ang", "The legend of Ang")

@naruto.introduce
def character_intro():
    print(f"I am {naruto.name} and i can use {naruto.ability}")

character_intro()
