def solution(my_string, indices):
    my_string = list(my_string)
    for index in indices:
        my_string[index] = ''
    
    return ''.join(my_string)