size_string = input("Insert size: ")
size_list = size_string.split()
attribute_string = input("Insert energy, health, energy loss, health loss: ")
attribute_list = attribute_string.split()


M = int(size_list[0])
N = int(size_list[1])
A = int(attribute_list[0])
B = int(attribute_list[1])
P = int(attribute_list[2])
Q = int(attribute_list[3])

maps = []
for i in range(M):
    maps.append(list(input()))

def print_map():
    for i in range(len(maps)):
        print(*maps[i], end=' ')
        print()

# print_map()
# print(A,B,P,Q)


def track(a,b):
    """ use global variables """
    global A
    global B
    global M
    gkibal N
    global P
    global Q

    """ reach destination """
    if a == M and b == N:
        print(A)
        print(B)

    if maps[a-1][b-1] == "x":
        

    

    

    