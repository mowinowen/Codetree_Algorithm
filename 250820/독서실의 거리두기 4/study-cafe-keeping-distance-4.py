import sys

N = int(input())
seat = input()

# Please write your code here.

seat = list(seat)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if seat[i] == '0' and seat[j] == '0':
            seat[i] = '1'
            seat[j] = '1'

            idxs = [k for k in range(N) if seat[k] == '1']
            
            tmp_ans = sys.maxsize
            for k in range(1, len(idxs)):
                tmp_ans = min(tmp_ans, idxs[k] - idxs[k - 1])
            
            ans = max(tmp_ans, ans)
            
            seat[i] = '0'
            seat[j] = '0'

print(ans)