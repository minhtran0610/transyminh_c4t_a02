equal = []
left = []
right = []
arr = []

n = int(input())
final = []
for i in range (n):
    arr.append(int(input()))

pivot = arr[0]
equal.append(pivot)
for i in range (1, n):
    if arr[i] < pivot:
        left.append(arr[i])
    elif arr[i] > pivot:
        right.append(arr[i])
    else:
        equal.append(arr[i])

def add_element(a, final):
    for i in range (len(a)):
        final.append(a[i])
    return final

add_element(left, final)
add_element(equal, final)
add_element(right, final)
print(*final, sep=' ')

