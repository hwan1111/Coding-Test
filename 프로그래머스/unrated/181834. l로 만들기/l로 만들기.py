def solution(myString):
    ord_list = [ord(myString[i]) for i in range(len(myString))]
    for i in range(len(ord_list)):
        if ord_list[i] < 108:
            myString = myString[:i] + 'l' + myString[i+1:]
    return myString