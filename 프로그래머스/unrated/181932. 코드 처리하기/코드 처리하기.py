def solution(code):
    mode = 0
    ret = []
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx%2 == 0:
                    ret.append(code[idx])
            else:
                mode = 1
        else:
            if code[idx] != '1':
                if idx%2 == 1:
                    ret.append(code[idx])
            else:
                mode = 0
    
    ret = ''.join(ret)
    if ret:
        return ret
    else:
        return 'EMPTY'