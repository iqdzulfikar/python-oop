"""
Cara python membuat setter getter adalah dengan membuat sebuah instance variable atau methodnya
menjadi properti. Dengan cara menambahkan decorator @property.

"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):  # getter
        return self.__name

    @name.setter  # setter
    def name(self, value):
        self.__name = value

    @name.deleter  # deleter
    def name(self):
        self.__name = None

    @property
    def age(self):  # getter
        return self.__age

    @age.setter  # setter
    def age(self, value):
        if value < 18:
            self.__age = 18
        elif value > 30:
            self.__age = 30
        else:
            self.__age = value

    @age.deleter  # deleter
    def age(self):
        self.__age = None


person = Person("rifqi", 25)

# getter
print(person.name)
print(person.age)

# setter
person.name = "dzulfikar"
person.age = 15

# getter
print('\n')
print(person.name)
print(person.age)

# deleter
del person.name
del person.age

# getter
print('\n')
print(person.name)
print(person.age)
