x = int(input())
for i in range (x):
    n = int(input())
    b = 5
    count = 0
    a = 1
    while (a>0):
        a = n//b
        count += a
        b *= 5
    print(count)
    



