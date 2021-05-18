RC = input("Insert row and column: ")
size = list(RC)
size.pop(1)
m = int(size[0])
n = int(size[1])

field = []
for i in range(m):
    field.append(list(input()))

# print(field)
# print(field[0])
visited = [[False for i in range(n)] for j in range(m)]
# print(visited)

def print_field(field):
    for i in range(len(field)):
        print(*field[i], end=' ')
        print()

print_field(field)

number_of_tufts = 0

# def able_to_move(x,y):
#     global m
#     global n
#     if x == m-1 and y>0 and y<n-1:
#         if field[x][y+1] == "#" or field[x][y-1] == "#" or field[x-1][y] == "#";
#             return True
#         else:
#             return False
#     elif x == m-1 and y == 0:
#         if field[x][y+1] == "#" or field[x-1][y] == "#":
#             return True
#         else:
#             return False
#     elif x == m-1 and y == n-1:
#         if field[x-1][y] == "#" or field[x][y-1] == "#":
#             return True
#         else:
#             return False
#     elif x == 0 and y>0 and y<n-1:
#         if field[x+1][y] == "#" or field[x][y+1] == "#" or field[x][y-1] == "#":
#             return True
#         else:
#             return False
#     elif x == 0 and y == 0:
#         if field[x+1][y] == "#" or field[x][y+1] == "#":
#             return True
#         else:
#             return False
#     elif x == 0 and y == n-1:
#         if field[x+1][y] == "#" or field[x][y-1] == "#":
#             return True
#         else:
#             return False

def is_grass(x,y):
    global m
    global n
    if x < 0 or y < 0 or x == m or y == n:
        return
    else:
        if field[x][y] == "#":
            return True

def able_to_move(x,y):
    if is_grass(x,y+1) or is_grass(x+1,y) or is_grass(x-1,y) or is_grass(x,y-1):
        return True
    else:
        return False

def track(x,y):
    global m
    global n
    global number_of_tufts
    # legal check
    if (x>=m or y>=n or x<0 or y<0 or visited[x][y] or visited[m-1][n-1] or field[x][y] == "." or not able_to_move(x,y)):
        number_of_tufts += 1
        return

    else:
        # print(x, y)
        visited[x][y] = True
        track(x+1,y)
        track(x-1,y)
        track(x,y+1)
        track(x,y-1)

for i in range(m):
    for j in range(n):
        # print(i,' ',j)
        # print(field[i][j])
        if not visited[i][j] and field[i][j] == "#":
            track(i,j)
            break

print(number_of_tufts)