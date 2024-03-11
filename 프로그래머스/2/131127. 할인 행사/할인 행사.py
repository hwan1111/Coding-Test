from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dic = {want[i]:number[i] for i in range(len(want))}

    for i in range(len(discount)):
        if want_dic == Counter(discount[i:i+10]):
            answer += 1

    return answer