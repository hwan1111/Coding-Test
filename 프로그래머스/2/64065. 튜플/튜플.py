def solution(s):
    s = s[1:-1]  # 바깥 대괄호 제거

    groups = []
    cur = []
    buf = ""     # 숫자를 누적할 버퍼

    for ch in s:
        if ch.isdigit():
            buf += ch
        elif ch == '{':
            cur = []
        elif ch == ',':
            # 숫자 끝
            if buf:
                cur.append(int(buf))
                buf = ""
        elif ch == '}':
            # 집합 하나 종료
            if buf:
                cur.append(int(buf))
                buf = ""
            if cur:
                groups.append(cur)
                cur = []

    # 길이 순 정렬 후 튜플 복원
    groups.sort(key=len)
    seen = set()
    answer = []
    for g in groups:
        for x in g:
            if x not in seen:
                seen.add(x)
                answer.append(x)
    return answer
