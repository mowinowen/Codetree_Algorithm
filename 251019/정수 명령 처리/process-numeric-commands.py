N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception('Stack is empty')
        return self.items.pop()

    def top(self):
        if self.empty():
            raise Exception('Stack is empty')
        return self.items[-1]

s = Stack()

for c, v in zip(command, value):
    if c == 'push':
        s.push(v)
    elif c == 'pop':
        print(s.pop())
    elif c == 'size':
        print(s.size())
    elif c == 'empty':
        if s.empty():
            print(1)
        else:
            print(0)
    else:
        print(s.top())