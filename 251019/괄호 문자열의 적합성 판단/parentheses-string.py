str = input()

# Please write your code here.
stack = []
for i in str:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) == 0:
            stack.append(i)
        else:
            stack.pop()

if len(stack) == 0:
    print('Yes')
else:
    print('No')