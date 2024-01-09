import re

def solution(my_str):
    list0 = re.findall(r'[0-9]+', my_str)
    
    return sum(list(map(int, list0)))