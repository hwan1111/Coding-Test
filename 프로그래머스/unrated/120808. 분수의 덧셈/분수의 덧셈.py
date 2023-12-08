def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(num1, den1, num2, den2):
    common_den = den1 * den2
    new_num1 = num1 * den2
    new_num2 = num2 * den1

    sum_num = new_num1 + new_num2

    divisor = GCD(sum_num, common_den)

    result_num = sum_num // divisor
    result_den = common_den // divisor

    return [result_num, result_den]