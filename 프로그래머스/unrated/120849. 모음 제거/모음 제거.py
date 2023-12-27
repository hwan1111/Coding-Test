def solution(my_str):
    vowel = ('a,e,i,o,u')
    for i in vowel:
        my_str = my_str.replace(i, '')
    
    return my_str