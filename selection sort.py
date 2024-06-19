unsort=[9,7,5,8,10,26,44,3,1]
sort=[]
while unsort:
    min_val=min(unsort)
    sort.append(min_val)
    unsort.remove(min_val)
print(sort)