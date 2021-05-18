n = int(input("Enter chessboard size: "))
Q = []
for i in range(n):
    Q.append(0)
def queen_recursion(Q,r):
    if r == n:
        return Q
    else:
        for j in range (n):
            legal = True
            for i in range (r):
                if Q[i] == j or Q[i] == j + r - i or Q[i] == j - r + i:
                    legal = False
            if legal:
                Q[r] = j
                queen_recursion(Q,r+1)

queen_recursion(Q, 0)        
print(Q)    

    