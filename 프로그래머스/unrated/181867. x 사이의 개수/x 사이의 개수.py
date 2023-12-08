def solution(myString):
    answer = []
    S = myString.split('x')
    for i in range(len(S)):
        answer.append(len(S[i]))
    return answer