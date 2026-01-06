import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bomb_inplace(grid):
    """
    [메모리 최적화 핵심 1]
    격자 전체를 복사(zip)하지 않고, 열(Col) 단위로 하나씩 처리하여
    메모리 피크(Peak)를 낮춥니다.
    """
    for j in range(n):
        # 1. 현재 열(j)에서 0이 아닌 값만 추출
        stack = [grid[i][j] for i in range(n) if grid[i][j] != 0]
        
        # 2. 투 포인터 로직 (이전과 동일)
        while True:
            if not stack:
                break
            
            is_exploded = False
            next_stack = []
            i = 0
            length = len(stack)
            
            while i < length:
                current_val = stack[i]
                start = i
                i += 1
                
                # 연속된 같은 숫자 찾기
                while i < length and stack[i] == current_val:
                    i += 1
                
                count = i - start
                
                if count < m:
                    next_stack.extend(stack[start:i])
                else:
                    is_exploded = True
            
            if not is_exploded:
                break
            stack = next_stack
            
        # 3. 결과를 다시 격자(grid)에 반영 (위쪽은 0으로 채움)
        # stack의 크기만큼 아래부터 채우고, 나머지는 0
        limit = n - len(stack)
        for i in range(n):
            if i < limit:
                grid[i][j] = 0
            else:
                grid[i][j] = stack[i - limit]
                
    return grid

def rotate(g):
    # 회전은 어쩔 수 없이 새로운 리스트가 생성되지만,
    # bomb 함수에서 메모리를 아꼈으므로 충분합니다.
    return list(map(list, zip(*g[::-1])))

# === 메인 로직 ===

# 1. 초기 폭발
bomb_inplace(grid)

# [메모리 최적화 핵심 2] 튜플 대신 해시값 저장
history = {} 

for turn in range(k):
    # 2. 회전 후 폭발
    grid = rotate(grid)
    bomb_inplace(grid) # grid 자체가 수정됨
    
    # 격자 상태의 해시(Hash)값 생성
    # 튜플을 통째로 딕셔너리에 넣지 않고, 정수형 해시값만 저장
    # 매우 드물게 해시 충돌 가능성이 있지만, 알고리즘 문제에서는 대부분 통과됩니다.
    
    current_key = hash(tuple(val for row in grid for val in row))
    
    if current_key in history:
        prev_turn = history[current_key]
        cycle_len = turn - prev_turn
        remaining_turns = k - 1 - turn
        
        steps_to_do = remaining_turns % cycle_len
        
        for _ in range(steps_to_do):
            grid = rotate(grid)
            bomb_inplace(grid)
        break
    
    history[current_key] = turn

ans = sum(len([x for x in row if x != 0]) for row in grid)
print(ans)