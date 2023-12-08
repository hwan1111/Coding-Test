#10951, A+B -4
#입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.

while True :
    try :
        A, B = map(int, input().split())
        print(A + B)
    except : break