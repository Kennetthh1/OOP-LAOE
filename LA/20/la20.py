class Adowbow:
    def __init__(self, meat,dry_season, wet_season, ):
        self.meat = meat
        self.__dry__season = dry_season
        self.wet__season = wet_season
       
    
    def __str__(self, me):
        return f"Ang adowbow ko ay {self.meat}, {self.__dry__season}, { self.wet__season}"
    def tama_ba_ito(self, oo):
        if not oo:
            return self.__dry__season
        else:
            return "MERON!"
    
adowbong_dry = Adowbow("chikin", "watir, asin" , "tuyo,asukal")
adowbow2 = Adowbow("baka", "watir" , "tuyo, imissyyou")
adowbo3 = Adowbow("Pork", "water" , "Onyon, asin Asukal")
print(adowbong_dry.tama_ba_ito(True))

'''print(adowbow2)
print(adowbo3)'''
