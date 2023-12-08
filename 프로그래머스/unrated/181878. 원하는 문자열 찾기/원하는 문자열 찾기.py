def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    return int(True if pat in myString else False)