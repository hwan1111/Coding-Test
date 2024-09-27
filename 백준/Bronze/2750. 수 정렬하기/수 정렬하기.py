def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + mid + quick_sort(right)

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    
    arr = quick_sort(arr)
    for i in range(N):
        print(arr[i])
    