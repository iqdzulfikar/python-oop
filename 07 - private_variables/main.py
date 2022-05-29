# 07 - Private Variables
class Hero:
    # class variables
    jumlah = 0
    __iniclassvar_private = 2
    _iniclassvar_protected = 3

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "ini private"

        # ini contoh variables dgn identifier protected
        self._ini_protected = "nilai awal protected"


lina = Hero("lina", 100)
# lina.__private = "testing"  # variable ini berbeda dengan variable __private di dalam classnya, dan akan dibuatkan vairables baru
# print(lina.__private) #  ERROR <- karena private
print(lina.__dict__)
print(lina._ini_protected)
lina._ini_protected = "ubah nilai protected"
print(lina.__dict__)
print(lina._ini_protected)

print(Hero.__dict__)
# print(Hero.__iniclassvar_private) # ini class variable protected
print(Hero._iniclassvar_protected)
