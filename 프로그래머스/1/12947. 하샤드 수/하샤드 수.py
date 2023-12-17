def solution(x):
    digits = [int(digit) for digit in str(x)]
    return True if x%sum(digits) == 0 else False