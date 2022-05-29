# 16 - Multiple Inhetiance
class  A:
    def method_a(self):
        print("Ini adalah method A")

class B:
    def method_b(self):
        print("Ini adalah method B")

class C(A, B):
    pass

object = C()

object.method_a()
object.method_b()