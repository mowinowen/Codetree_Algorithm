from collections import deque

n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
dq = deque()
for c, n in zip(cmd, num):
    if c == 'push_front':
        dq.appendleft(n)
    elif c == 'push_back':
        dq.append(n)
    elif c == 'pop_front':
        print(dq.popleft())
    elif c == 'pop_back':
        print(dq.pop())
    elif c == 'size':
        print(len(dq))
    elif c == 'empty':
        print(0 if dq else 1)
    elif c == 'front':
        print(dq[0])
    elif c == 'back':
        print(dq[-1])