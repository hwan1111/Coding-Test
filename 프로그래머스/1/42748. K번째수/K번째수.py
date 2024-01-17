def solution(arr, commands):
    answer = []
    current = []
    for i, j, k in commands:
        current = sorted(arr[i-1:j])
        answer.append(current[k-1])
        current = []
    
    return answer