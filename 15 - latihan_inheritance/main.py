# 15 - Latihan Inheritance
from Hero import HeroIntelligent, HeroStrength

lina = HeroIntelligent('lina')
slardar = HeroStrength('slardar')

lina.showinfo()
slardar.showinfo()

lina.gainexp = 200
slardar.gainexp = 250

lina.showinfo()
slardar.showinfo()
