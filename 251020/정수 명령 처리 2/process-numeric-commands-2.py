from collections import deque

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty():
            raise Exception("Queue is not empty")
        
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception("Queue is not empty")
        
        return self.dq[0]

q = Queue()
for c, a in zip(command, A):
    if c == 'push':
        q.push(a)
    
    elif c == 'pop':
        print(q.pop())
    
    elif c == 'size':
        print(q.size())
    
    elif c == 'empty':
        if q.empty():
            print(1)
        else:
            print(0)
    
    elif c == 'front':
        print(q.front())