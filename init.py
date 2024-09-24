class Stack:
    def __init__(self):
        self.stack = []
    
    def empty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.empty():
            value = self.stack.pop()
            return value
    
    def top(self):
        if not self.empty():
            value = self.stack.pop()
            return value

s = Stack()

print(s.empty())
s.push(1)
s.push(2)
print(s.empty())
s.push(2)
print(s.pop())