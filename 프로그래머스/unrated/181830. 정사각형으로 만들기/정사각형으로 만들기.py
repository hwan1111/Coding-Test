def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    if row_len < col_len:   #열의 길이가 행보다 길때: 열에 원소를 추가
        for i in range(col_len - row_len):
            arr.append([0]*col_len)
    elif row_len > col_len: #행의 길이가 열보다 길때: 행에 원소를 추가
        for i in range(row_len):
            for j in range(row_len - col_len):
                arr[i].append(0)
    return arr