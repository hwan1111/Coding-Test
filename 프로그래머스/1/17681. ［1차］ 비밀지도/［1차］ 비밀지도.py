def solution(n, arr1, arr2):
    map = []
    current = ''
    for i in range(n):
        row1_i = bin(arr1[i])[2:]
        row2_i = bin(arr2[i])[2:]
        if len(row1_i) != n:
            row1_i = '0'*(n - len(row1_i)) + row1_i
        if len(row2_i) != n:
            row2_i = '0'*(n - len(row2_i)) + row2_i
        
        for j in range(n):
            if int(row1_i[j]) == 0 and int(row2_i[j]) == 0:
                current += ' '
            else:
                current += '#'
            
        map.append(current)
        current = ''
    return map