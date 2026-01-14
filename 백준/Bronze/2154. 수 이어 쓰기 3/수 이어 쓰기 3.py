def solution(n):
    concat_num = ''
    for i in range(1, n + 1):
        concat_num += str(i)

    find_num = str(n)
    for i in range(len(concat_num) - len(find_num) + 1):
        if find_num == concat_num[i:i + len(find_num)]:
            return i + 1
    return len(concat_num) - len(find_num) + 1

if __name__ == "__main__":
    n = int(input())
    result = solution(n)
    print(result)