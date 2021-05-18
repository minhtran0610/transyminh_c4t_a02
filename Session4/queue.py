class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        s = ""
        for i in range (len(self.items)-1,0,-1):
            s += str(self.items[i]) + " "
        if not self.is_empty():
            s += str(self.items[0])
        return s

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def insert(self, n):
        self.items.append(n)

    def remove(self):
        return self.items.pop(0)
        
        

        