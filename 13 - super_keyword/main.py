# 13 - Super
class Hero:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def showinfo(self):
        print("{} dengan health: {}".format(self.__name, self.__health))


class HeroIntelligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)  # menggunakan super() keyword
        super().showinfo()


class HeroStrength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200)  # menggunakan super() keyword
        super().showinfo()


lina = HeroIntelligent("lina")
axe = HeroStrength("axe")
