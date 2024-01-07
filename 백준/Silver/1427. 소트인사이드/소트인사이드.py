def sortinside(num):
    answer = ''.join(sorted(str(num), reverse=True))

    return int(answer)

N = int(input())
print(sortinside(N))