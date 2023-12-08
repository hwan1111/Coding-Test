#10807, 개수 세기
#배열을 입력받고 v를 찾는 문제

N = int(input())
Num_list = list(map(int, input().split()))
v = int(input())

print(Num_list.count(v))