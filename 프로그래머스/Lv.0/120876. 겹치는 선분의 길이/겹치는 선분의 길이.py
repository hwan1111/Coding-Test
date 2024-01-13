def solution(lines):
    answer = set()
    for i, a in enumerate(lines):
        for b in lines[i + 1:]:
                answer |= set(range(a[0], a[1])) & set(range(b[0], b[1]))
    return len(answer)