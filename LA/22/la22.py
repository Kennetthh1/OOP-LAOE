class Birthdayan:
    def __init__(self, party_theme, list_of_pods):
        self.party_theme = party_theme
        self.list_of_pods = list_of_pods
    def foods(self):
        print(f"Here are the foods Crispy Puta, Pancit" )
        self.__secret_dish()
    def __secret_dish(self):
        print(f"Here are the list of sikrit desh {self.list_of_pods}")

animey = Birthdayan("PancitUmay", "palabok")
marvel = Birthdayan("Kalbonatics","EightBallers")
ih = Birthdayan("nakakapagud", "litsun")

animey.foods()
marvel.foods()
ih.foods()
