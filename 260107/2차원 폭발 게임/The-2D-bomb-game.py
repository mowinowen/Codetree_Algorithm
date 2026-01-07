import sys

n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
if m == 1:
    print(0)

else:
    for i in range(n):
        col = [numbers_2d[j][i] for j in range(n) if numbers_2d[j][i]]
        
        while True:
            isbool = False
            if len(col) > 1:
                curr = col[0]
                cnt = 1
                new_col = []

                for num in col[1:]:
                    if curr == num:
                        cnt += 1
                    else:
                        if cnt < m:
                            new_col += [curr] * cnt
                        else:
                            isbool = True
                        curr = num
                        cnt = 1
                
                if cnt < m:
                    new_col += [curr] * cnt
                else:
                    isbool = True
                
            if not isbool:
                break
            col = new_col
        
        col = [0] * (n - len(col)) + col
        
        for j in range(n):
            numbers_2d[j][i] = col[j]
    
    for _ in range(k):
        # 시계 방향 회전
        numbers_2d = list(map(list, zip(*numbers_2d[::-1])))
        
        for i in range(n):
            col = [numbers_2d[j][i] for j in range(n) if numbers_2d[j][i]]
            
            while True:
                isbool = False
                if len(col) > 1:
                    curr = col[0]
                    cnt = 1
                    new_col = []

                    for num in col[1:]:
                        if curr == num:
                            cnt += 1
                        else:
                            if cnt < m:
                                new_col += [curr] * cnt
                            else:
                                isbool = True
                            curr = num
                            cnt = 1
                    
                    if cnt < m:
                        new_col += [curr] * cnt
                    else:
                        isbool = True
                    
                if not isbool:
                    break
                col = new_col
            
            col = [0] * (n - len(col)) + col
            
            for j in range(n):
                numbers_2d[j][i] = col[j]

    print(n ** 2 - sum(row.count(0) for row in numbers_2d))