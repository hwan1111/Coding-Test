def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer.append(arr[a:b+1])
    answer = [data for inner_list in answer for data in inner_list]
    return answer