def solution(myStr):
    myStr = myStr.replace('a', 'c')
    myStr = myStr.replace('b', 'c')
    myStr = myStr.split('c')
    myStr = [i for i in myStr if len(i) > 0]
    if not myStr:
        return ["EMPTY"]
    else:
        return myStr