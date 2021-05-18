num_string = input("Insert a and b: ")
initial_list = num_string.split()
# print(initial_list)

a = int(initial_list[0])
b = int(initial_list[1])

# print(a,b)

def greatest_common_divisor(a,b):
    # print(a)
    # print(b)
    if a%b == 0:
        print(b)
        return
    else:
        greatest_common_divisor(b,a%b)

greatest_common_divisor(a,b)