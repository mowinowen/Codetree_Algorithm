import sys

# 재귀 깊이 설정 (필요시)
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bomb_col(col):
    """
    한 열(1D 리스트)에 대해 폭발 및 중력을 처리하는 함수
    groupby 대신 인덱스 스캔(Two-pointer) 방식을 사용하여 메모리를 절약함
    """
    # 1. 0 제거 (중력 적용) - 리스트 컴프리헨션은 빠르고 메모리 효율적임
    current_col = [x for x in col if x != 0]
    
    while True:
        if not current_col:
            return []
        
        is_exploded = False
        new_col = []
        i = 0
        length = len(current_col)
        
        # 2. 선형 스캔으로 연속된 그룹 확인
        while i < length:
            current_val = current_col[i]
            count = 1
            j = i + 1
            
            # 다음 값들이 현재 값과 같은지 확인
            while j < length and current_col[j] == current_val:
                count += 1
                j += 1
            
            # M개 이상이면 폭발 (new_col에 담지 않음)
            if count >= m:
                is_exploded = True
            else:
                # M개 미만이면 유지 (값 복사)
                # extend([val] * count) 방식이 리스트 슬라이싱보다 가벼움
                new_col.extend([current_val] * count)
            
            # 인덱스 점프
            i = j
        
        # 변화가 없으면 루프 종료
        if not is_exploded:
            return current_col
        
        # 변화가 있으면 업데이트 후 다시 검사 (연쇄 폭발)
        current_col = new_col

def simulation_step(current_grid):
    # 1. 1차 폭발 (Transpose -> Bomb -> Transpose)
    # zip(*grid)는 튜플을 반환하므로 map(list, ...) 필요
    cols = list(map(list, zip(*current_grid)))
    bombed_cols = []
    for col in cols:
        processed = bomb_col(col)
        # 앞에 0 채우기 (중력)
        bombed_cols.append([0]*(n - len(processed)) + processed)
    
    current_grid = list(map(list, zip(*bombed_cols)))
    
    # 2. 반시계? 아니면 문제 조건의 회전 (여기선 기존 코드대로 90도 회전 적용)
    # 기존 코드 로직: zip(*new_grid[::-1]) -> 시계 방향 90도 회전
    current_grid = list(map(list, zip(*current_grid[::-1])))
    
    # 3. 2차 폭발 (Transpose -> Bomb -> Transpose)
    cols = list(map(list, zip(*current_grid)))
    bombed_cols = []
    for col in cols:
        processed = bomb_col(col)
        bombed_cols.append([0]*(n - len(processed)) + processed)
    
    return list(map(list, zip(*bombed_cols)))

# === 메인 실행 로직 ===
history = {} # { 1차원_튜플_상태 : turn_index }

# 초기 상태 기록
initial_key = tuple(val for row in grid for val in row)
history[initial_key] = -1 # 시작 전 상태

for turn in range(k):
    grid = simulation_step(grid)
    
    # 1차원 튜플로 변환 (메모리 최소화: chain이나 중첩 루프 사용)
    # chain.from_iterable보다 제너레이터 표현식이 메모리를 덜 쓸 때가 있음
    grid_key = tuple(val for row in grid for val in row)
    
    if grid_key in history:
        prev_turn = history[grid_key]
        cycle_len = turn - prev_turn
        remaining_turns = k - 1 - turn
        
        # 남은 횟수를 사이클 길이로 나눈 나머지 계산
        remaining_turns %= cycle_len
        
        # 나머지 만큼만 추가 실행
        for _ in range(remaining_turns):
            grid = simulation_step(grid)
        break
    
    history[grid_key] = turn

# 결과 계산
ans = sum(len([x for x in row if x != 0]) for row in grid)
print(ans)