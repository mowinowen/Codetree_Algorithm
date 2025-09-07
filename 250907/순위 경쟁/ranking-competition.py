n = int(input())
count_dict = {'A': 0, 'B': 0, 'C': 0}
curr = {'A', 'B', 'C'}
ans = 0

for _ in range(n):
    ci, si = input().split()
    si = int(si)
    count_dict[ci] += si
    curr_tmp = set()

    max_val = max(count_dict.values())
    for k in count_dict:
        if count_dict[k] == max_val:
            curr_tmp.add(k)
    
    if curr != curr_tmp:
        ans += 1
    
    curr = curr_tmp

print(ans)