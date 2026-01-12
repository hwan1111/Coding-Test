import re
from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    set_str1 = [str1[i:i+2] for i in range(len(str1) - 1) if re.fullmatch(r'[a-z]{2}', str1[i:i+2])]
    set_str2 = [str2[i:i+2] for i in range(len(str2) - 1) if re.fullmatch(r'[a-z]{2}', str2[i:i+2])]
    
    c1 = Counter(set_str1)
    c2 = Counter(set_str2)
    inter = list((c1 & c2).elements())
    union = list((c1 | c2).elements())
    
    jacard = len(inter) / len(union) if len(union) != 0 else 1
    return int(jacard * 65536)