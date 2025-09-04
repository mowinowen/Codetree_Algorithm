a, b, c = map(int, input().split())

print(max(b - (a + 2) + 1, (c - 2) - b + 1))