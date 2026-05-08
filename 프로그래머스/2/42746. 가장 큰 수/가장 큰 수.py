def solution(numbers):
    num_str = list(map(str, numbers))
    num_str.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(num_str)
    
    return str(int(answer))