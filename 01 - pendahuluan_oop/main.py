# 01 - Apa itu OOP
class Hero:  # template class
    pass


# Object / instance (instantsiate)
hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "Sniper"
hero1.health = 100

hero2.name = "Sven"
hero2.health = 200

hero3.name = "Ucup"
hero3.health = 1_000

print(hero1)
print(hero1.__dict__)
print(hero1.name)