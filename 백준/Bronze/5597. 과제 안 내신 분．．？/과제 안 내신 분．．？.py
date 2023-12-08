Attendance = [i for i in range(1, 31)]  #1번부터 30번까지 출석부
for _ in range(1, 29) :                 #28번 입력 받음
    n = int(input())                    #출석번호n을 입력 받음
    Attendance.remove(n)                #입력받은 출석번호는 리스트에서 삭제함
for j in range(2) :              
    print(Attendance[j])            