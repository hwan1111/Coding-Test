def solution(n):
    digits = [int(digit) for digit in str(n)]
    sorted_digits = sorted(digits, reverse=True)
    
    return int(''.join(map(str, sorted_digits)))