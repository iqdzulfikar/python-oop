"""
08 - Enkapsulasi
Setter -> method utk mensetting /mengatur nilai variable
Getter -> method utk mengambil nilai dari suatu variable
"""


class Hero:

    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    # contoh getter
    def getname(self):
        return self.__name

    def gethealth(self):
        return self.__health

    # contoh setter
    def diserang(self, serang_power):
        self.__health -= serang_power

    def setattackpower(self, new_value):
        self.__attack_power = new_value


# awal dari game
earthshaker = Hero("Earth Shaker", 50, 5)

print(earthshaker.__dict__)

# game berjalan
# earthshaker.__name = "windrunner" # ERROR <- karena instance variablenya private (__)
print(earthshaker.getname())
earthshaker.diserang(5)
print(earthshaker.gethealth())
