string = input("Nhap cac phan tu trong mang: ")
initial_list = string.split()
list_of_numbers = []
for i in range(len(initial_list)):
    list_of_numbers.append(int(initial_list[i]))
    # print(initial_list[i])

print(sum(list_of_numbers), sep=' ')
print(max(list_of_numbers), sep=' ')
print(min(list_of_numbers), sep=' ')