string = input("Nhap N va P: ")
list = string.split()
present = []

N = int(list[0])
P = int(list[1])

for i in range(N):
    present.append(input("Nhap qua: "))

def buy_present(time, P):
    if time > P:
        # print(present)
        return
    
    taken_out = present.pop(0)
    present.append(taken_out)
    present.append(taken_out)
    # print(present)
    buy_present(time+1, P)

def print_present():
    if len(present)%2 == 0:
        print(present[len(present)//2-1])
        print(present[len(present)//2])
    else:
        print(present[len(present)//2])

buy_present(1,P)
print_present()


    
    

