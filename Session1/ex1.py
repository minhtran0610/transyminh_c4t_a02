class Person:
    name = ""
    age = 0
    def __init__(self, name, yob):
        self.name = name
        self.age = 2019 - yob

ten = input("Moi ban nhap ten: ")
nam_sinh = int(input("Moi ban nhap nam sinh: "))  
nguoi1 = Person(ten, nam_sinh)
print("Tuoi cua ban la:", nguoi1.age)
