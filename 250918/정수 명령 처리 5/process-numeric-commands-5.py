N = int(input())
arr = []

for _ in range(N):
    command = input().split()
    if len(command) == 2:
        if command[0] == 'push_back':
            arr.append(int(command[1]))
        else:
            print(arr[int(command[1]) - 1])
    
    else:
        if command[0] == 'pop_back':
            arr.pop()
        else:
            print(len(arr))