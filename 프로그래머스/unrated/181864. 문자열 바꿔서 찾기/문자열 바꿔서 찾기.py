def solution(myString, pat):
    myString = myString.replace("A", "0")
    myString = myString.replace("B", "1")
    myString = myString.replace("0", "B")
    myString = myString.replace("1", "A")

    return int(True if pat in myString else False)
