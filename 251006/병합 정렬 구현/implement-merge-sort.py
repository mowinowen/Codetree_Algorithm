n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
merged_arr = [0] * n
def merge(arr, low, mid, high):
    i, j = low, mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arr[j]
            k += 1
            j += 1
    
    while i <= mid:
        merged_arr[k] = arr[i]
        k += 1
        i += 1
    
    while j <= high:
        merged_arr[k] = arr[j]
        k += 1
        j += 1
    
    for k in range(low, high + 1):
        arr[k] = merged_arr[k]
    
    return arr


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

merge_sort(arr, 0, n - 1)
print(*merged_arr)