class Adowbow:
    def __init__(self, meat,dry_season, wet_season, ):
        self.meat = meat
        self.__dry__season = dry_season
        self.wet__season = wet_season
       
    
    def __str__(self, me):
        return f"Ang adowbow ko ay {self.meat}, {self.__dry__season}, { self.wet__season}"
    
    def tama_ba_ito(self):
            return self.__meat
    
    def update(self, bagong_value):
         self.__meat = bagong_value
        
adowbong_dry = Adowbow("chikin", "watir, asin" , "tuyo,asukal")
adowbow2 = Adowbow("baka", "watir" , "tuyo, imissyyou")
adowbo3 = Adowbow("Pork", "water" , "Onyon, asin Asukal")

adowbong_dry.update("sige")
print(adowbong_dry.tama_ba_ito())


'''print(adowbow2)
print(adowbo3)'''
