from itertools import product
import sys
input = sys.stdin.readline

n = int(input())

# Please write your code here.
ans = 0
if n == 1:
    print(1)
else:
    for val in product(range(1, 5), repeat = n):
        cnt_list = [0, 0, 0, 0]
        tmp = val[0]
        cnt = 1
        isbool = True
        for i in range(1, n):
            if tmp == val[i]:
                cnt += 1
            else:
                if cnt % tmp != 0:
                    isbool = False
                    break
                tmp = val[i]
                cnt = 1
        
        if cnt % tmp != 0:
            isbool = False

        if isbool:
            ans += 1

    print(ans)