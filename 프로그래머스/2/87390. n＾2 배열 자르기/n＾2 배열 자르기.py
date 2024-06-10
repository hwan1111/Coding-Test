def solution(n, left, right):
    answer = []
    for index in range(left, right + 1):
        # 1차원 배열의 인덱스를 2차원 배열의 좌표로 변환
        row = index // n
        col = index % n
        # (row, col) 위치의 값은 max(row, col) + 1
        answer.append(max(row, col) + 1)
    return answer
