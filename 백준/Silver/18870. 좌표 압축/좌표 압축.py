import sys
input = sys.stdin.readline

N = int(input())
cordinate = list(map(int, input().split()))
unique_list = sorted(list(set(cordinate)))

unique_dict = {unique_list[i] : i for i in range(len(unique_list))}
for i in cordinate:
    print(unique_dict[i], end = ' ')