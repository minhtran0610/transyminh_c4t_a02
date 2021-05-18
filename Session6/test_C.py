s = input()
count_n = 0
count_i = 0
count_e = 0
count_t = 0

for i in s:
    if i == "n":
        count_n += 1
    elif i == "i":
        count_i += 1
    elif i == "e":
        count_e += 1
    elif i == "t":
        count_t += 1
    else:
        pass

if (3 <= count_n < 5):
    n = 1
elif (count_n < 3):
    n = 0
else:
    n = ((count_n-5)//2)+2

print(min(count_e//3, count_i, n, count_t))
