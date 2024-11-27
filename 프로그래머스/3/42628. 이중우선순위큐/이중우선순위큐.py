def solution(operations):
    num = []
    op = []
    
    for k in operations:
        if k[0] == 'I':
            num.append(int(k[1:]))
        else:
            if len(num) == 0:
                continue
                
            if k[2] == '1':
                num.remove(max(num))
            if k[2] == '-':
                num.remove(min(num))
        
    return [max(num), min(num)] if num else [0, 0]