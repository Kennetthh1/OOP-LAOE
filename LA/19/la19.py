class Adowbow:
    def __init__(self, meat,dry_season, wet_season, ):
        self.meat = meat
        self.dry_season = dry_season
        self.wet_season = wet_season
        
    
    def __str__(self):
        return f"Ang adowbow ko ay {self.meat}, {self.dry_season}, { self.wet_season}"
    
adowbong_dry = Adowbow("chikin", "watir, asin" , "tuyo,asukal")
adowbow2 = Adowbow("baka", "watir" , "tuyo, imissyyou")
adowbo3 = Adowbow("Pork", "water" , "Onyon, asin Asukal")
print(adowbong_dry)
print(adowbow2)
print(adowbo3)
