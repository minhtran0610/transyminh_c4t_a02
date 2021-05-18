def trib(a):
    if a==1 or a==2 or a==3:
        return 1
    elif a>3:
        return trib(a-1) + trib(a-2) + trib(a-3)
    else:
        print("Invalid")
n = int(input("Enter index: "))
print("Number:", trib(n))
