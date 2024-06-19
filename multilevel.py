class a:
    def a(self):
        print("a")
class b(a):
    def b(self):
        print("a")
        print("b")
class c(b):
    def c(self):
        print("a")
        print("b")
        print("c")
d=a()
d.a()
d=b()
d.b()
d=c()
d.c()