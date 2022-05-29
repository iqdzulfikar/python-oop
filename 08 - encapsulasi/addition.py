class Base:

    def __init__(self):
        self._a = 2  # protected member
        self.__b = 3  # private member


class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print('Calling protected member of Base class ', self._a)
        # print('Try to calling private member of Base class ', self.__c) # ERROR


obj1 = Base()
obj2 = Derived()
