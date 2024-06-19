class student:
    def __init__(self,nm,ag,gn):#init is private method
        self.name=nm
        self.age=ag
        self.gen=gn
st1=student("uday",20,'m')
print(st1.name,st1.age,st1.gen)
        
class std:
    def __init__(self):
        self.name=None
        self.age=None
        self.gender=None 
st2=std()
st2.name=input()
st2.age=int(input())
st2.gen=input()
print(st2.name,st2.age,st2.gen)


a=input()
b=int(input())
c=input()
st3=student(a,b,c)

print(st3.name,st3.age,st3.gen)


