class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        if len(items) <= limit:
            self.items = items


    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if (target not in self.items):
            return -1
        else:
            index = self.items.index(target)
            distance = len(self.items) - index
            return distance - 1
