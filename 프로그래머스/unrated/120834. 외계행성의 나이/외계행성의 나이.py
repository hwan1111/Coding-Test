def solution(age):
    answer = ''
    PROGRAMMER_962 = 'abcdefghij'
    for i in str(age):
        answer += PROGRAMMER_962[int(i)]
    
    return answer