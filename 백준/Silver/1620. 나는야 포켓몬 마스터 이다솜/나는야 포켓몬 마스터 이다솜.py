import sys

# 입력을 더 빠르게 받기 위한 설정
input = sys.stdin.readline

n, m = map(int, input().split())

# 번호로 이름을 찾기 위한 리스트 (1번부터 시작하므로 0번은 더미 데이터)
num_to_name = [0] * (n + 1)
# 이름으로 번호를 찾기 위한 딕셔너리
name_to_num = {}

for i in range(1, n + 1):
    name = input().strip() # .strip()으로 개행문자(\n) 제거 필수!
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(m):
    query = input().strip()
    
    if query.isdigit():
        # 입력이 숫자라면 리스트에서 바로 출력
        print(num_to_name[int(query)])
    else:
        # 입력이 문자라면 딕셔너리에서 번호(값)를 찾아 출력
        print(name_to_num[query])