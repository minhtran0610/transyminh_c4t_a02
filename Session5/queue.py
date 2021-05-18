class Queue:
    def __init__(self, x):
        self.items = []
        self.capacity = x

    def __str__(self):
        s = ""
        for i in range (len(self.items)-1):
            s += str(self.items[i]) + " "
        if not self.is_empty():
            s += str(self.items[len(self.items)-1])
        return s

    def insert(self, n):
        if len(self.items) == self.capacity:
            return False
        else:
            self.items.insert(0,n)
            return True

    def remove(self):
        return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def is_full(self):
        pass