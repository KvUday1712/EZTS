# [2,1,0,1,1,2,0,0]=>[0,0,0,1,1,1,2,2]
a=(2,1,0,1,1,2,0,0)
c0=0
c1=1
c2=2
for i in range(len(a)):
    if a[i]==1:
        c0+=0
    elif a[i]==1:
        c1+=1
    else:
        c2+=c1
j=0
while c0>0:
    a[j]=0
    j=j+1
    c0=c0-1
while c1>0:
    a[j]=1
    j=j+1
    c0=c0-1
while c2>0:
    a[j]=2
    j=j+1
    c0=c0-1
print(a)


            