class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def describeSpiderman(self):
         print(f"The name of this Spiderman is {self.name} with the age of {self.age} ")

class Tobey(Spiderman):
        def __init__(self, name, age , movieTitle):
            super().__init__(name, age)
            self.movieTitle = movieTitle
            
class Andrew(Spiderman):
        def __init__(self, name, age , movieTitle):
            super().__init__(name, age)
            self.movieTitle = movieTitle
            
class Tom(Spiderman):
        def __init__(self, name, age , movieTitle):
            super().__init__(name, age)
            self.movieTitle = movieTitle
            

gagamboy = Tobey("Tobias Vincent Maguire", 49 , "Spiderman BlackRed")
gagamboy2 = Andrew("Andrew Russell Garfield", 41 , "Spiderman BlueGreen")
gagamboy3 = Tom("Thomas Stanley Holland ", 28 , "Spiderman LightBlue")

print(f"{gagamboy.name.upper()} {gagamboy.movieTitle}") 
print("------------------------------------------------")
print(f"{gagamboy2.name.upper()} {gagamboy2.movieTitle}") 
print("------------------------------------------------")
print(f"{gagamboy3.name.upper()} {gagamboy3.movieTitle}") 
print("------------------------------------------------")
