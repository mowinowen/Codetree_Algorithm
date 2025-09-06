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
    if lx < rx < bx or bx < rx < lx:
        print(abs(lx - bx) + 1)
    else:
        print(abs(lx - bx) - 1)

elif bx == rx == lx:
    if ly < ry < by or by < ry < ly:
        print(abs(ly - by) + 1)
    else:
        print(abs(ly - by) - 1)

else:
    print(abs(lx - bx) + abs(ly - by) - 1)