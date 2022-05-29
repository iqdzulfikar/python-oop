"""
    Inheritance - the capability of one class to derive or inherit the properties and methods from another class.
    The benefits of inheritance are:
    1. It represents real-world relationships as well.
    2. It provides reusability of a code. We don't have to write the same code again and again.
    3. etc.

1. Single Inheritance -> When a child in class inherits from only one parent class,
it's called Single Inheritance. We saw an example below.
"""


class Person(object):

    def __init__(self, name):
        self.name = name

    def getname(self):  # getter
        return self.name

    def isemployee(self):
        return False


class Employee(Person):

    # override
    def isemployee(self):
        return True


person = Person("rifqi")
print(person.getname(), person.isemployee())
person = Employee("dzulfikar")
print(person.getname(), person.isemployee())
