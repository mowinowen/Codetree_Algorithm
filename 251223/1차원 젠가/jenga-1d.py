n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
def update_blocks(s, e):
    temp = [blocks[i] for i in range(len(blocks)) if s - 1 > i or i > e - 1]
    return temp

blocks = update_blocks(s1, e1)
blocks = update_blocks(s2, e2)

print(len(blocks))
for val in blocks:
    print(val)