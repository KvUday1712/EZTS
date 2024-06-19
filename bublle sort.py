n=[8,2,17,4,88,7,5 ]
for j in range(0,len(n)-1):
    for i in range(0,len(n)-1):
        if(n[i]>n[i+1]):
            n[i],n[i+1]=n[i+1],n[i]
print(n)
print(min(n))   

