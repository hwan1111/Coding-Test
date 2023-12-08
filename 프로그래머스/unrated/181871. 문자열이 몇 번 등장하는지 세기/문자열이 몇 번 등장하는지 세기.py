def solution(myString, pat):
    answer = 0
    strlist = [myString[i:i+len(pat):] for i in range(len(myString))]
    for s in strlist:
        if pat == s:
            answer += 1
    return answer