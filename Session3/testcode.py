s = input("Enter a string with aterisk: ")
temp = []
li = []
result = ""
for v in s:
    if v == "*":
        letter = temp.pop()
        li.append(letter)
    else:
        temp.append(v)
for i in range(len(li)):
    result += str(li[i])
print(result)
