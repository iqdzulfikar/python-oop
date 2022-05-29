class Hero:
    def __init__(self, name):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attpower_pool = [0, 10, 20, 30, 40, 50]
        self.armor_pool = [0, 1, 2, 3, 4, 5]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def showinfo(self):
        print("{}: \n\tlevel: {} \n\thealth: {} \n\tattpower: {} \n\tarmor: {}".format(self.__name, self.__level,
                                                                                       self.__health, self.__attpower,
                                                                                       self.__armor)
              )

    @property
    def health_pool(self):
        pass

    @property
    def attpower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def level_up(self):
        pass

    @property
    def gainexp(self):
        pass

    @health_pool.setter
    def health_pool(self, in_health):
        self.__health_pool = in_health

    @attpower_pool.setter
    def attpower_pool(self, in_attpower):
        self.__attpower_pool = in_attpower

    @armor_pool.setter
    def armor_pool(self, in_armor):
        self.__armor_pool = in_armor

    @gainexp.setter
    def gainexp(self, input):
        self.__exp += input
        if (self.__exp >= 100):
            self.level_up = self.__exp // 100
            self.__exp %= 100

    @level_up.setter
    def level_up(self, input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attpower = self.__attpower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]


class HeroIntelligent(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 50, 100, 150, 200, 250]
        self.attpower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.level_up = 1


class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 200, 300, 400, 500, 600]
        self.attpower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 2, 4, 6, 8, 10]
        self.level_up = 1
