def solution(s):
    en_to_num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    answer = ''
    current = ''
    for char in s:
        if char.isalpha():
            current += char
            if current in en_to_num:
                answer += en_to_num[current]
                current = ''
        else:
            answer += char
    
    return int(answer)