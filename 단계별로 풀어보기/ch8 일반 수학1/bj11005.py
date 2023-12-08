#11005, 진법 변환2
#반대 방향으로 진법을 변환하는 문제

def decimal_to_base_B(N, B):
    Dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,\
           'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19,\
           'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29,\
           'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
    Rev_Dic = {v: k for k, v in Dic.items()}
    result = []

    while N > 0:
        mod = Rev_Dic[N%B]
        result.append(mod)
        N//=B

    while result:
        print(result.pop(), end = "")

N, B = map(int, input().split())
decimal_to_base_B(N, B)