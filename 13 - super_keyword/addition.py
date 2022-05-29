class Person():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Name : " + self.name)
        print("ID Number : "+str(self.id))

class Employee(Person):

    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary : Rp. {self.salary:,}")


person = Person("rifqi", 11)
person.display()
print("\n")
person = Employee("dzulfikar", 3, 8_000_000)
person.display()