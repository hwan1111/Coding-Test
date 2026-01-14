N, K = map(int, input().split())

def Josephus(N, K):
    people = list(range(1, N + 1))
    result = []
    idx = 0

    while people:
        idx = (idx + K - 1) % len(people)
        result.append(people.pop(idx))

    return result

result = Josephus(N, K)
print("<" + ", ".join(map(str, result)) + ">")