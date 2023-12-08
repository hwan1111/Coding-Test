def solution(myString):
    return sorted(filter(bool, myString.split('x')))