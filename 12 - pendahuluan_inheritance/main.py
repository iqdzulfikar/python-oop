"""
12 - Inheritance (Pewarisan)

"""


class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health


class HeroIntelligent(Hero):
    pass


class HeroStrength(Hero):
    pass


lina = Hero("lina", 100)
techies = HeroIntelligent('techies', 50)
axe = HeroStrength('axe', 200)

print(lina.__dict__)
print(help(type(techies)))
print(techies.__dict__)
print(axe.__dict__)
