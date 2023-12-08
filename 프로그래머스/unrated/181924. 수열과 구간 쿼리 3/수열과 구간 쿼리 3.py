def solution(arr, queries):
    for j in range(len(queries)):
        arr[queries[j][0]], arr[queries[j][1]] = arr[queries[j][1]], arr[queries[j][0]]
    
    return arr