def solution(arr):
    X = []
    for el in arr:
        for i in range(el):
            X.append(el)
    
    return X