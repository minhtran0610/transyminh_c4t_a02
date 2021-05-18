class Person:
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

li = []
n = int(input("Nhap so nguoi: "))
def create_person(a):
    ten = input("Nhap ten nguoi thu "+ str(a) +": ")
    tuoi = int(input("Nhap tuoi nguoi thu "+ str(a) +": "))
    nguoi = Person(ten, tuoi)  
    return nguoi
for i in range(n):
    nguoi = create_person(i+1)
    li.append(nguoi)
for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if li[i].age > li[j].age:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
for i in range(len(li)-1):
    print(li[i].name, end=', ')
print(li[len(li)-1].name)


