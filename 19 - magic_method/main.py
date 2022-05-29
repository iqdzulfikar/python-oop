# 19 - Magic Method
class Mangga:

    # dibawah ini adalah contoh-contoh magic method (method yg sudah dimiliki python)
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):  # ini digunakan ketika melakukan debugging
        return "Debugging : \n\tMangga {}, dengan jumlah = {}".format(self.name, self.count)

    # ini akan di panggil lebih dulu dibanding __repr__()
    def __str__(self):  # ini digunakan ketika program sudah jadi (produksi)
        return "Produksi : \n\tMangga {}, dengan jumlah = {}".format(self.name, self.count)

    def __add__(self, other):
        return self.count + other.count

    def __dict__(self):
        return "Ini dict mangga"


belanja1 = Mangga("aromanis", 10)
belanja2 = Mangga("mana lagi", 20)
print(belanja1)

print(belanja1 + belanja2)  # memanggil __add__()
print(belanja1.__dict__())
