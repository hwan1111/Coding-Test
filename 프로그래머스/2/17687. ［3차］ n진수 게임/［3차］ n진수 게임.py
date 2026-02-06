def solution(n, t, m, p):
    # 1. n진수 변환 함수
    def convert(num, base):
        if num == 0: return "0"
        digits = "0123456789ABCDEF"
        res = ""
        while num > 0:
            res += digits[num % base]
            num //= base
        return res[::-1]

    # 2. 전체 게임 문자열 만들기
    full_string = ""
    num = 0
    # 전체 인원 m명이 t번씩 돌아가려면 최소 t*m 길이의 문자열이 필요함
    while len(full_string) < t * m:
        full_string += convert(num, n)
        num += 1

    # 3. 내 순서(p)에 해당하는 글자만 골라내기
    # p-1 인덱스부터 시작해서 m(인원수)씩 건너뛰며 t개만큼 가져옴
    answer = full_string[p-1::m][:t]
    
    return answer