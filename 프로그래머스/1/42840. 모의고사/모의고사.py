def solution(answers):
    # 각 수포자의 답안 패턴을 길이에 맞게 반복
    supo_1 = [1, 2, 3, 4, 5] * ((len(answers) // 5) + 1)
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5] * ((len(answers) // 8) + 1)
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((len(answers) // 10) + 1)

    # 각 수포자가 맞힌 문제 수를 저장하는 변수
    i1, i2, i3 = 0, 0, 0
    
    # 답안과 비교하여 맞힌 문제 수를 계산
    for i in range(len(answers)):
        if answers[i] == supo_1[i]:
            i1 += 1
        if answers[i] == supo_2[i]:
            i2 += 1
        if answers[i] == supo_3[i]:
            i3 += 1
    
    # 각 수포자가 맞힌 문제 수를 리스트에 저장
    scores = [i1, i2, i3]

    # 가장 많이 맞힌 문제 수 찾기
    max_score = max(scores)

    # 가장 많이 맞힌 수포자 찾기
    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx + 1)  # 수포자의 번호는 1부터 시작하므로 +1

    # 오름차순 정렬하여 반환
    return sorted(result)
