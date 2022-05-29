# 18 - Diamond Problem (seperti Wajik)

class A:
    def show(self):
        print('Ini show A')


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


object = D()

"""
object akan memanggil method show() di class B (superclass yg pertama di sebutkan). Jika di class B tidak ada. 
Maka, ia akan memanggil di class C. Jika ternyata di class C masih tidak ada. Dia akan memanggil method di class A.
"""
object.show()
