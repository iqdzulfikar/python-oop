# 11 - Latihan Enkapsulasi (Getter dan Setter)

class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, att_power, armor):
        self.__name = name
        self.__health_standar = health
        self.__attpower_standar = att_power
        self.__armor_standar = armor
        self.__level = 1
        self.__exp = 0

        self.__health_max = self.__health_standar * self.__level
        self.__attpower = self.__attpower_standar * self.__level
        self.__armor = self.__armor_standar * self.__level

        self.__health = self.__health_max

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level: {} \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,
                                                                                       self.__level, self.__health,
                                                                                       self.__health_max,
                                                                                       self.__attpower, self.__armor)

    @property
    def gainexp(self):
        pass

    @gainexp.setter
    def gainexp(self, exp):
        self.__exp += exp

        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
            self.__health_max = self.__health_standar * self.__level
            self.__attpower = self.__attpower_standar * self.__level
            self.__armor = self.__armor_standar * self.__level

    def attack(self, enemy):
        self.gainexp = 50


slardar = Hero("slardar", 100, 5, 10)
axe = Hero("axe", 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print("\n" + slardar.gainexp)
print("\n" + slardar.info)
