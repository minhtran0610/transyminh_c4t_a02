n = int(input("Insert number of integers: "))
arr = []
for i in range (n):
    arr.append(int(input("Insert integer: ")))

def quick_sort_with_index(arr, first_index, last_index):
    if last_index-first_index < 1:
        return arr
    else:
        pivot = arr[last_index]
        lower = first_index - 1
        for i in range (first_index, last_index+1, 1):
            if arr[i] < pivot:
                lower += 1
                arr[i], arr[lower] = arr[lower], arr[i]
        arr[last_index], arr[lower+1] = arr[lower+1], arr[last_index]
        quick_sort_with_index(arr, first_index, lower)
        quick_sort_with_index(arr, lower+2, last_index)
        return arr

def quick_sort(arr):
    first_index = 0
    last_index = len(arr)-1
    quick_sort_with_index(arr, first_index, last_index)
    return arr

quick_sort(arr)
print(*arr, sep=' ')















