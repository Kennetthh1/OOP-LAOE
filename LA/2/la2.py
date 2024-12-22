class character:
    def __init__(self, hero, role):
        self.hero = hero
        self.role = role

student = character("YuZhong", "Fighter")
print(student.hero, student.role)
