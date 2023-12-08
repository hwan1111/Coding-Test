def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i]:
            for j in range(2*arr[i]):
                X.append(arr[i])
        else:
            for j in range(arr[i]):
                X.pop()
        
    return X