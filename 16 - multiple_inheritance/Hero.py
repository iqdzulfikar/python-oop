class Team:
    def setteam(self, team):
        self.team = team

    def showteam(self):
        print(self.team)


class TypeHero:
    def settype(self, type):
        self.type = type

    def showtype(self):
        print(self.type)


class Hero(Team, TypeHero):
    def __init__(self, name, health):
        self.name = name
        self.health = health


ucup = Hero('ucup', 100)
ucup.setteam('merah')
ucup.settype('cundang')

ucup.showteam()
ucup.showtype()
