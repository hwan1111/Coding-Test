def solution(picture, k):
    enlarge_k = []
    for pic in picture:
        for i in range(k):
            enlarge_k += [''.join([char * k for char in pic])]
    return enlarge_k