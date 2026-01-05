# 1269
# 대칭 차집합

len_A, len_B = map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

diff_A_B = set_A - set_B
diff_B_A = set_B - set_A
sym_union = diff_A_B.union(diff_B_A)

print(len(sym_union))