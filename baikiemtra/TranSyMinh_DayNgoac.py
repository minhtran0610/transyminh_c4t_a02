parentheses = list(input("Insert parentheses: "))
temp = []
is_valid = True

for v in parentheses:
    if v == "(":
        temp.append(v)

    if v == ")":
        if len(temp) == 0:
            is_valid = False
            break
        else:
            temp.pop()

if is_valid and len(temp) > 0:
    is_valid = False

print(is_valid)


