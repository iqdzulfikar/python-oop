# 10 - Getter dan Setter
class Hero:


    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {}\t : \n\thealth : {}".format(self.__name, self.__health)

    # menggunakan decorator property -> menganggap methods sebagai variable
    @property
    def info(self):
        return "name {}\t : \n\thealth : {}".format(self.name, self.__health)

    @property
    def armor(self):
        return self.armor

    # contoh syntax getter python
    @armor.getter
    def armor(self):
        return self.__armor

    # contoh syntax setter python
    @armor.setter
    def armor(self, armor):
        self.__armor = armor

    # deleter <- mengosongkan nilai pada suatu atribut (None)
    @armor.deleter
    def armor(self):
        print("Armor di delete")
        self.__armor = None



sniper = Hero('sniper', 100, 10)

print("Merubah Info")
print(sniper.info)
sniper.name = "Dadang"
print(sniper.info)

print("\nContoh Getter & Setter utk __armor")
print(f"Armor: {sniper.armor}")  # pemanggilan getter dalam python
sniper.armor = 50  # pemanggilan setter dalam python
print(f"Armor: {sniper.armor}")

print("\nContoh Deleter utk __armor")
del sniper.armor
print(f"Armor menjadi: {sniper.armor}")
