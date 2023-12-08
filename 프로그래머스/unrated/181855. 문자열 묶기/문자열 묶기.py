def solution(strArr):
    temp = []
    Arr = [0]*len(strArr)
    for i in strArr:
        Arr[len(i)] += 1
    
    return max(Arr)