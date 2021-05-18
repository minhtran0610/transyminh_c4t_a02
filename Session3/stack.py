class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        s = ""
        for i in range (len(self.items)-1):
            s += str(self.items[i]) + " "
        if not self.is_empty():
            s += str(self.items[len(self.items)-1])
        return s
        
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def push(self,x):
        self.items.append(x)
    
    def pop(self):
        return self.items.pop()
    
    def clear(self):
        self.items.clear()

