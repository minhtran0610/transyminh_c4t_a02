def fib(a):
    if a == 1 or a == 2:
        return 1
    elif a>2:
        return fib(a-1) + fib(a-2)
    else:
        print("Invalid")
n = int(input("Enter index: "))
print("Fibonacci number:", fib(n))