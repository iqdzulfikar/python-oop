# 14 - Override Methods
class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showinfo(self):
        print('showinfo() superclass')
        print("{} : \n\thealth: {}".format(self.name, self.health))


class HeroIntelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # ini contoh override methods
    def showinfo(self):
        print('showinfo() subclass')
        print("{} : \n\thealth : {}".format(self.name, self.health))


class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = HeroIntelligent('lina')
axe = HeroStrength('axe')

lina.showinfo()
print('\n')
axe.showinfo()
