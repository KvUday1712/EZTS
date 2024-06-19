class animal:
    def __init__(self,a,b):
        self.grass=a
        self.grasshoper=b
        print("constructor")
    def grasshoper(self):
        print("grasshoper eats grass")
        print("grass hoper eats 20 grams of grass")
        self.s=20
    def frog(self):
        print("frog eats grasshoper")
        self.f=self.s+25
        print("the frog has eaten 25 grasshopers")
    def snake(self):
        print("snake will eat frog")
        self.sn=self.f*self.s
        print("self.sn",self.sn)
t=animal()
t.grasshoper()
t.frog()
t.snake()

    
    