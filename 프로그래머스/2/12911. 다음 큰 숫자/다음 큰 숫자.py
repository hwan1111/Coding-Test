def count_ones_in_binary(num):
    return bin(num).count('1')

def solution(n):
    target_ones = count_ones_in_binary(n)
    answer = n + 1

    while count_ones_in_binary(answer) != target_ones:
        answer += 1

    return answer
