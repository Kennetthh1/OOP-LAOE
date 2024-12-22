class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability 
    def introduce(ramdom_parameter, some_function):
        def inner():
            print("Introducing...")
            some_function()
            print("This character is amazing!")
        return inner
        
ninTa = TekkenCharacter("Nina", "Fatal Judgement")

@ninTa.introduce
def character_intro():
    print(f"I am {ninTa.name} and I can use {ninTa.ability}")
        
character_intro()
        


    
