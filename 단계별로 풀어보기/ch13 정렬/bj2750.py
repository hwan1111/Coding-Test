#2750, 수 정렬하기
#시간 복잡도가 O(n²)인 정렬 알고리즘으로 풀 수 있습니다. 예를 들면 삽입 정렬, 거품 정렬 등이 있습니다.

def insert_sort(int_list):
    for i in range(1, len(int_list)):
        temp = int_list[i]
        prev = i -1
        while prev >= 0 and int_list[prev] > temp:
            int_list[prev + 1] = int_list[prev]
            prev -= 1
        int_list[prev + 1] = temp

    return int_list

n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

num_list = insert_sort(num_list)

for i in range(n):
    print(num_list[i])