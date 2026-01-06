import sys

# 빠른 입출력
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bomb(current_grid):
    # 1. 열(Column) 단위 처리를 위해 전치 (Transpose)
    cols = list(map(list, zip(*current_grid)))
    result_cols = []
    
    for col in cols:
        # 0을 제거한 숫자들만 추출 (중력 적용)
        stack = [x for x in col if x != 0]
        
        while True:
            if not stack:
                break
                
            is_exploded = False
            next_stack = []
            i = 0
            length = len(stack)
            
            # 투 포인터로 연속된 그룹 확인
            while i < length:
                current_val = stack[i]
                j = i + 1
                
                # 같은 숫자가 연속되는 구간 찾기 (j 이동)
                while j < length and stack[j] == current_val:
                    j += 1
                
                count = j - i
                
                if count < m:
                    # m개 미만이면 살아남음 (next_stack에 복사)
                    # 리스트 슬라이싱보다 extend가 조금 더 효율적일 수 있음
                    next_stack.extend(stack[i:j])
                else:
                    # m개 이상이면 폭발 (next_stack에 추가하지 않음)
                    is_exploded = True
                
                # 다음 탐색 위치로 점프
                i = j
            
            # 폭발이 없었다면 루프 종료
            if not is_exploded:
                break
            
            # 폭발 후 상태 업데이트 (연쇄 반응 체크를 위해 반복)
            stack = next_stack

        # 앞쪽에 0을 채워서 길이 맞추기
        result_cols.append([0] * (n - len(stack)) + stack)
    
    # 다시 원래대로 전치하여 반환
    return list(map(list, zip(*result_cols)))

def rotate(g):
    # 시계 방향 90도 회전
    return list(map(list, zip(*g[::-1])))

# === 메인 로직 ===

# 1. 초기 폭발 1회 수행
grid = bomb(grid)

history = {} # { 격자상태_튜플 : 방문한_turn_인덱스 }

for turn in range(k):
    # 2. 회전 후 폭발
    grid = rotate(grid)
    grid = bomb(grid)
    
    # 격자 상태를 1차원 튜플로 변환 (메모리 절약 및 검색 속도 향상)
    
    grid_key = tuple(val for row in grid for val in row)
    
    if grid_key in history:
        prev_turn = history[grid_key]
        cycle_len = turn - prev_turn       # 주기(Cycle) 계산
        remaining_turns = k - 1 - turn     # 남은 횟수 (현재 turn은 끝났으므로 -1)
        
        # 남은 횟수를 주기로 나눈 나머지만큼만 더 수행하면 됨
        steps_to_do = remaining_turns % cycle_len
        
        for _ in range(steps_to_do):
            grid = rotate(grid)
            grid = bomb(grid)
        break # 시뮬레이션 종료
    
    # 상태 기록
    history[grid_key] = turn

# 결과 계산
ans = sum(len([x for x in row if x != 0]) for row in grid)
print(ans)