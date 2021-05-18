m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

print("Nhap ban do: ")

maps = []
visited = [[False for i in range(n)] for j in range(m)]
for i in range(m):
    row = input()
    maps.append(list(row))
ways = []
ways_len = 9999999999
optimal_ways = []

def print_maps():
    for i in range(m):
        print(*maps[i])
    print()

def track(i,j):
    global ways_len, optimal_ways
    # print(i,j)
    # print(visited)
    # print_maps()
    if (visited[m-1][n-1] or i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or maps[i][j] == "#"):
        return
    
    maps[i][j] = 'x'
    visited[i][j] = True
    ways.append([i,j])

    if (i == m-1 and j == n-1):
        # print_maps()
        if (len(ways)-1 < ways_len):
            ways_len = len(ways)-1
            optimal_ways = ways.copy()

    track(i+1,j)
    track(i-1,j)
    track(i,j+1)
    track(i,j-1)

    visited[i][j] = False
    maps[i][j] = '.'
    ways.pop()
track(0,0)

print("Do dai duong di ngan nhat: ",ways_len)
print(*optimal_ways)