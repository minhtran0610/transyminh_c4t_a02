def fact(n):
    if n == 0:
        return 1
    elif n > 0:
        return n*fact(n-1)
    else:
        return "Invalid"
n = int(input("Enter a number: "))
print(fact(n))