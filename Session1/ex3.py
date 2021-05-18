n = int(input("Nhap so phan tu: "))
list_of_number = []
for i in range(n):
    number = int(input("Nhap phan tu: "))
    list_of_number.append(number)
for j in range(len(list_of_number)-1):
    for k in range(j+1,len(list_of_number)):
        if list_of_number[j] > list_of_number[k]:
            temp = list_of_number[j]
            list_of_number[j] = list_of_number[k]
            list_of_number[k] = temp
print(*list_of_number)