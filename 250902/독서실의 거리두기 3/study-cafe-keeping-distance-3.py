N = int(input())
seats = list(input())

pos = [i for i, j in enumerate(seats) if j == '1']
gap = [pos[i] - pos[i - 1] for i in range(1, len(pos))]
print(min(max(gap) // 2, min(gap)))