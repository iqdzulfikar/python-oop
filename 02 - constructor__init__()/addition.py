"""
    Constructor - Generally used for instantiating an object.
The task of constructors is to initialize (assign value) to the data members of the class
when an object of the class is created.

Syntax of constructor declaration:
    1. Default Constructor -> a simple constructor which doesn't accept any args.
    def __init__(self)

    2. Parameterized Constructor -> takes its first arg as a reference to the instance being constructed known
    as self and the rest of the args are provided by the programmer.
    def __init__(self,(if the class have an args))
        # body of the constructor

    Destructor - called when an object gets destroyed. In python, destructors are not needed as much as in C++,
    because python has a garbage collector that handles memory management automatically.

    The __del__() method is known as a destructor method in python. It's called when all references to the object
    have been deleted.
"""


class Addition:
    count = 0

    # parameterized constructor
    def __init__(self, first_arg, second_arg):
        # instance variables
        self.first = first_arg
        self.second = second_arg

    def display(self):
        print("First Agument: " + str(self.first))
        print("Second Argument : " + str(self.second))
        print("{} + {} = {}".format(self.first, self.second, self.__calculate()))

    def __calculate(self):  # private methods
        self.count = self.first + self.second
        return self.count

    # def __del__(self):
    #     print("Destructor called, Addition Deleted.")


addition = Addition(1000, 2000)
addition.display()
print("\n")
# addition.__del__()
print("\n")
addition.display()
