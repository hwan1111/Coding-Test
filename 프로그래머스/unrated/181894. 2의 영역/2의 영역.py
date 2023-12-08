def solution(arr):
    answer = []
    result = []
    for i in range(len(arr)):
        if arr[i] == 2:
            result += arr[i:]
            break
    
    for j in range(len(result)):
        if result[j] == 2:
            answer = result[:j+1]
    
    if answer:
        return answer
    else:
        return [-1]