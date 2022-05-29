# 09 - Static Methods dan Class Methods

class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku utk object, tidak dengan class
    def getjumlah(self):
        return Hero.__jumlah

    # method ini hanya berlaku utk class, tidak dengan object
    # def getjumlah1():  # warning seharusnya dibuat staticmethods <- karena tidak memiliki argument
    #     return Hero.__jumlah

    # ini adalah contoh static method (decorator) di python, nempel ke class dan objectnya
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah

    #
    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(sniper.getjumlah())
# print(Hero.getjumlah()) # Tidak berlaku utk classnya, karena arguments object (self)
# print(sniper.getjumlah1()) # Tidak berlaku utk objectnya, karena tidak ada argument object (self)

# berlaku kedua2nya (object & classnya) <- static methods
print(f"\nobject akses static method: {sniper.getjumlah2()}")
print(f"class akses static method: {sniper.getjumlah2()}")

# berlaku utk keduanya (object dan class) <- class methods
print(f"\nobject akses class method: {sniper.getjumlah3()}")

rikimaru = Hero("rikimaru")
print(f"class akses class method: {rikimaru.getjumlah3()}")
print(f"class akses class method: {Hero.getjumlah3()}")
