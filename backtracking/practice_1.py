permutation = []

def track(_level, _maxlevel):
    if _level == _maxlevel+1:
        print(permutation)
        return

    for i in range (1, _maxlevel+1):
        if not visited[i]:
            permutation.append(i)
            visited[i] = True
            track(_level+1, _maxlevel)
            visited[i] = False
            permutation.pop()

n = int(input("Enter a number: "))
visited = [False] * (n+1)
track(1,n)




