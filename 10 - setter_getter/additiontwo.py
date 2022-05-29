# Contoh memnbuat variable private dan setter

class Map:

    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

    __geek = geek


class MapSubClass(Map):

    def geek(self, key, value):
        for index in zip(key, value):
            self.list.append(index)
