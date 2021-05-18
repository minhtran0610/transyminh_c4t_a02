class Node:
    content = None
    Next = None
    def __init__(self):
        pass


class LinkedList:
    def __init__(self):
        self.head = []
    
    def push(self):
        pass

    def is_empty(self):
        if len(self.head) == 0:
            return True
        else:
            return False

    def __str__(self):
        s = ""
        if self.is_empty():
            s = "<<E>>"
        else:
            for i in range(len(self.head)-1):
                s += str(self.head[i]) + "->"
            if not self.is_empty():
                s += str(self.head[len(self.head)])
        return s

    def add_first(self, d):
        pass


    def remove_first(self):
        pass

    def add_last(self):
        pass

    def remove_last(self):
        pass

    def find(self):
        pass

