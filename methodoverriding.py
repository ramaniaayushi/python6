class A:
    def show (self):
        print("show from clas A")
class B(A):
    def show(self):
        super().show()
        print("show from class B")
class C(A):
    def show(self):
     super().show()
    print("show from class c")
class D(B,C):
    def show(self):
     super().show()
    print("show from class D")
d1=D()
d1.show()
