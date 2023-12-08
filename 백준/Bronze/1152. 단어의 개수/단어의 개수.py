S = input()
temp = 0
if " " in S :
    temp = S.count(" ") + 1
    if S[0] == " " : 
        temp = temp - 1
    if S[-1] == " " : 
        temp = temp - 1 
    print(temp)
else : print(1)