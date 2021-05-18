from collections import deque
parentheses = deque()
n = int(input("Number of parentheses: "))
if n%2 == 1:
    print("Invalid parentheses")
else:
    for i in range (n):
        parentheses.append(input("Enter parenthesis: "))
        print(parentheses)
    group_1=[]
    group_2=[]
    for i in range(n//2):
        group_1.append(parentheses.pop())
    for i in range(len(parentheses)):
        group_2.append(parentheses.pop())
    for i in range (len(group_1)):
        if group_1[i] == "(":
            for j in range(len(group_2)):
                if group_2[j] == ")":
                    print("Valid parentheses")
                else:
                    print("Invalid parentheses")
        else:
            print("Invalid parentheses")