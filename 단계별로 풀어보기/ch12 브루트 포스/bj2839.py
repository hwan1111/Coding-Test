#2839, 설탕 배달
#한때는 이 문제가 "기본 수학 1" 단계에 있었지만, 사실 브루트 포스로 푸는 게 더 쉽습니다.

def sugar(N):
    result = []

    for i in range(N//3 +1):
        remaining = N - i * 3
        if remaining % 5 == 0:
            j = remaining // 5
            result.append((i, j))

    if len(result) == 0:
        return -1
    else:
        min_sum = min(sum(pair) for pair in result)
        return min_sum

N = int(input())
print(sugar(N))