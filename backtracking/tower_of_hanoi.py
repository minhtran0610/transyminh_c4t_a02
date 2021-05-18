n = int(input("Enter number of discs: "))
def move(n, source, aux, dest):
    if n == 1:
        print(source, "->", dest)
        return

    move(n-1, source, dest, aux)
    print(source, "->", dest)
    move(n-1, aux, source, dest)

move(n, "A", "B", "C")

