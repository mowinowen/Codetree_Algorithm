board = [list(input()) for _ in range(10)]

# Please write your code here.
for i in range(10):
    for j in range(10):
        if board[i][j] == 'B':
            bx, by = i, j
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'L':
            lx, ly = i, j

if by == ry == ly:
    print(abs(lx - bx) + 1)

elif bx == rx == lx:
    print(abs(ly - by) + 1)

else:
    print(abs(lx - bx) + abs(ly - by) - 1)