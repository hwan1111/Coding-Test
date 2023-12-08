def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        min_num = -1
        result = []
        for j in range(queries[i][0], queries[i][1]+1):
            if arr[j] > queries[i][2]:
                min_num = arr[j]
                result.append(min_num)
                min_num = min(result)
                
        answer.append(min_num)
    
    return answer