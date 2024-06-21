n = int(input("Enter a number: "))
if n < 1000:
    print("Zero commas")
else:
    count = (len(str(n)) - 1) // 3
    print(count)