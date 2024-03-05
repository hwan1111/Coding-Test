def testpair(exp) -> bool:
    S = []
    for st in exp:
        if st in "([{":
            S.append(st)
        elif st in ")]}":
            if not S:
                return False
            symbol = S.pop()
            if (st == ')' and symbol != '(') or (st == '}' and symbol != '{') or (st == ']' and symbol != '['):
                return False
        
    if not S:
        return True
    return False

def solution(s):
    answer = 0
    x = len(s) - 1
    rotated_s = []
    for i in range(x):
        rotated_list = [s[j] for j in range(i, len(s))] + [s[j] for j in range(i)]
        rotated_s.append(rotated_list)
        if testpair(''.join(rotated_s[i])):
            answer += 1
    
    return answer