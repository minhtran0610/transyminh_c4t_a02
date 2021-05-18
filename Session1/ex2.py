n = int(input("Enter a number: "))
if n<0:
    print("So ban nhaplon")
result = 1
for i in range(n):
    result *= (i+1)
print("n! =",result)