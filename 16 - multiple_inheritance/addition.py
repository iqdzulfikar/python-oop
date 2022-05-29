"""
    Multiple Inheritance - When a child class inherits from multiple parent classes,
    it's called multiple inheritance. Or when we have a child and grandchild relationship.

    Unlike java, python shows multiple inheritance.
"""


class Base:

    # Constructor
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


class Child(Base):

    def __init__(self, name, age, address):
        Base.__init__(self, name)
        self.__age = age
        self.__address = address

    def getaddress(self):
        return self.__address

    def get_age(self):
        return self.__age


child = Child("rifqi", 10, "bandung")
print(child.name)
print(child.get_age)
print(child.getaddress())
print(child.getname())
