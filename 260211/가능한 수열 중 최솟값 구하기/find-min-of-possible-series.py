import sys
input = sys.stdin.readline

n = int(input())

# Please write your code here.
result = []

def check(result):
    c = len(result) - 1
    if c != 0:
        for i in range((c + 1)// 2):
            if result[c - i - i - 1 : c - i] == result[c - i : c + 1]:
                return False
    
    return True

def dfs(cnt):
    if cnt == n:
        print(''.join(list(map(str, result))))
        sys.exit()
    
    for i in range(4, 7):
        result.append(i)
        if check(result):
            dfs(cnt + 1)
        
        result.pop()
    
dfs(0)