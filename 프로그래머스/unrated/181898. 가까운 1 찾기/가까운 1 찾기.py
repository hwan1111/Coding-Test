def solution(arr, idx):
    for i, value in enumerate(arr):
        if (i >= idx) and (value == 1):
            return i
    return -1