# 04 - methods - Methods
class Hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, name, health, power, armour):
        # instance variable
        self.name = name
        self.health = health
        self.power = power
        self.armour = armour
        Hero.jumlah_hero += 1

    # methods tanpa argumen dan nilai kembalian (return)
    def siapa(self):
        print("Namaku adalah: " + self.name)

    # methods dengan arguments (parameter)
    def healtup(self, up):
        self.health += up

    # methods dengan return (nilai kembalian)
    def gethealth(self):
        return self.health


hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("mario bros", 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healtup(10)
print(hero1.gethealth())
