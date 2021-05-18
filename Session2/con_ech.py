def fact(n):
    if n == 0:
        return 1
    elif n > 0:
        return n*fact(n-1)
    else:
        return "Invalid"
def arr(a,b):
    return fact(a)//(fact(a-b)*fact(b))
n = int(input("Insert length of river: "))
ways = 0
for i in range (n//2 + 1):
    ways += arr(n-i,i)
print("Number of ways:",ways)