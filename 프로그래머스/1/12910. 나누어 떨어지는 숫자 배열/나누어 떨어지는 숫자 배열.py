def solution(arr, div):
    answer = [num for num in arr if num%div == 0]
    if answer:
        return sorted(answer)
    else:
        return [-1]