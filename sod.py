#sum of digits of a no using recursion 7 6 5 4
def s(n):   
    if n==0:
        return 0
    return n%10+s(n//10)
print()



