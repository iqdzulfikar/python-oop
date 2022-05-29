# 2 - Constructor __init__()

class Hero:
    """
    __init__ -> magic keyword (inisialisasi objectnya)
    """

    def __init__(self, input_nama, input_health, input_power, input_armour):  # self adalah object classnya
        self.name = input_nama
        self.health = input_health
        self.power = input_power
        self.armour = input_armour


#  Inisialisasi Object
hero1 = Hero("sniper", 100, 1, 4)
hero2 = Hero("mirana", 100, 15, 1)
hero3 = Hero("ucup", 1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
