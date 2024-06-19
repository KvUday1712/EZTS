def pow(n,m):
    if m==0:
        return 1
    if m==1:
        return n
    else:
        return n*pow(n,m-1)
print(pow(2,3))
