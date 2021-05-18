arr = []
n = int(input("Enter list size: "))
for i in range (n):
    arr.append(int(input("Enter number: ")))
print(arr)
a = arr[n-1]
for i in range (n-2,-1,-1):
    if arr[i] < a:
        arr[i+1] = a
        a = arr[i]
        print(arr)
        break
    else:
        arr[i+1] = arr[i]
        print(arr)

if a < arr[0]:
    arr[0] = a
    print(arr)

    
        
