n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def heapify(n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and arr[l] > arr[largest]:
        largest = l
    
    if r <= n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(n, largest)

def heap_sort(n):
    for i in range(n // 2, 0, -1):
        heapify(n, i)
    
    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(i - 1, 1)

heap_sort(n)
print(*arr[1:])