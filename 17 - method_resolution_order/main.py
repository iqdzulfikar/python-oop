# method resolution order (multiple inheritance)
class A:

    def show(self):  # method resolution order
        print('ini show A')


class B:
    def show(self):  # method resolution order
        print('ini show B')


class C(A, B):
    pass


ucup = C()

# dia akan memanggil method resolution order A (tergantung urutan superclass yg mana dl)
ucup.show()
