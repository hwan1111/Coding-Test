List = []                       #입력 받을 리스트 선언
NewList = []                    #42로 나눌 리스트를 따로 선언
for _ in range(10) :            
    i = int(input())        
    List.append(i)              #입력받은 값을 List에 추가
    NewList.append(List[_] % 42)
my_set = set(NewList)           #set으로 중복 값을 제거
my_list = list(my_set)          #set을 다시 리스트로 만들고
print(len(my_list))             #리스트의 길이 = 나머지의 갯수