# m = int(input("Enter length: "))
# n = int(input("Enter width: "))
# maze = []
# for i in range (n):
#     maze.append([])
#     for j in range(m):
#         maze[i].append("-")

# obs_num = int(input("Enter number of obstacles: "))
# for i in range(obs_num):
#     x = int(input("x = "))
#     y = int(input("y = "))
#     maze[y][x] = "#"
m = 4
n = 3
test_maze = [
    ["-", "#", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "#", "-"]
]        

def print_maze(maze):
    for i in range(len(maze)):
        print(*maze[i], end=' ')
        print()

print_maze(test_maze)

path = []
visited = []
path_list = []
path_length = []

def legal_position(maze,x,y):
    global m
    global n
    if x <= m-1 and y <= n-1 and x >= 0 and y >= 0 and maze[y][x] == "-" and [x,y] not in visited:
        return True
    else:
        return False

def solve(maze,x,y):
    print("solve",x,y)
    global m
    global n
    if x == m-1 and y == n-1:
        path.append([x,y])
        path_list.append(path.copy())
        path_length.append(len(path))
        wrong = path.pop()
        if len(path) == 0:
            return
        else:
            x = path[len(path)-1][0]
            y = path[len(path)-1][1]
            visited.append(wrong)
            solve(maze,x,y)

    else:
        path.append([x,y])
        # print(*path)
        # print()
        if legal_position(maze,x+1,y):
            solve(maze,x+1,y)
        elif legal_position(maze,x,y+1):
            solve(maze,x,y+1)
        elif legal_position(maze,x-1,y):
            solve(maze,x-1,y)
        elif legal_position(maze,x,y-1):
            solve(maze,x,y-1)
        else:
            wrong = path.pop()
            if len(path) == 0:
                print("No appropriate move")
                return
            else:
                x = path[len(path)-1][0]
                y = path[len(path)-1][1]
                visited.append(wrong)
                solve(maze,x,y)

solve(test_maze,0,0)
print(path_list)
print(path_length)
            


    

       




