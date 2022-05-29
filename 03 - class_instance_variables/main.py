# 03 - class_instance_variables - Class dan Instance Variable
class Hero:
    # class variabel <- variable punyanya si class
    count = 0

    def __init__(self, name, health, power, armour):
        # instance variable (atribut si object)
        self.name = name
        self.health = health
        self.power = power
        self.armour = armour
        Hero.count += 1  # menghitung jumlah object hero yang dibuat
        print("Membuat object Hero dengan nama " + name)


hero1 = Hero("sniper", 100, 10, 4)
print(Hero.count)  # print 1
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.count)  # print 2
hero3 = Hero("ucup", 100, 100, 0)
print(Hero.count)  # print 3

print(Hero.__dict__)  # akan menampilkan atribut/class variable (ex: count)
