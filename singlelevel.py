class a:
    def a(self):
        print("a")
class b(a):
    def b(self):
        print("b")
c=a()
c.a()
c=b()
c.b()
    