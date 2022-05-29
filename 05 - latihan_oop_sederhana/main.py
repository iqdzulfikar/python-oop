# 05 - latihan_oop_sederhana - Latihan Sederhana (Game Sederhana saling serang :D)
class Hero:

    def __init__(self, name, health, attack_power, armour):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armour = armour

    def menyerang(self, hero_lawan):
        print(self.name + " Menyerang " + hero_lawan.name)
        hero_lawan.diserang(self, self.attack_power)

    def diserang(self, hero_lawan, power_lawan):
        print(self.name + " Diserang " + hero_lawan.name)
        attack_diterima = (power_lawan / self.armour)
        print(f"Serangan {hero_lawan.name} terasa = {str(attack_diterima)}")
        self.health -= attack_diterima
        print(f"Darah {self.name} tersisa = {str(self.health)}\n")


sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)

sniper.menyerang(rikimaru)
rikimaru.menyerang(sniper)
