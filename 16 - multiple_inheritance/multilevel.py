"""
Multilevel Inheritance - features of the base class and the derived class are further inherited
into the new derived class. This is similar to a relationship representing a child and grandfather.
"""
class Abah():

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Bapak(Abah):

    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Abah.__init__(self, grandfathername)

class Aku(Bapak):

    def __init__(self, myname, fathername, grandfathername):
        self.myname = myname
        Bapak.__init__(self,fathername, grandfathername)


    def print_name(self):
        print("My Name\t\t\t\t\t: {} \nMy Father Name\t\t\t: {} \nMy Grand Father Name\t: {} ".format(self.myname, self.fathername, self.grandfathername))

rifqi = Aku("rifqi", "zaenal aripin", "abdulloh")
rifqi.print_name()

dzulfikar = Aku("dzulfikar", "zaenal aripin", "zae")
dzulfikar.print_name()