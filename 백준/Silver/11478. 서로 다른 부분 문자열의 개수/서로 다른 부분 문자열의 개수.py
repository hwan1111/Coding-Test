# 11478
# 서로 다른 부분 문자열의 개수

S = input()
unique_substrings_list = []
for substring in S:
    unique_substrings_list.append(substring)

for i in range(len(S)):
    for j in range(i+1, len(S)):
        unique_substrings_list.append(S[i:j+1])

print(len(set(unique_substrings_list)))