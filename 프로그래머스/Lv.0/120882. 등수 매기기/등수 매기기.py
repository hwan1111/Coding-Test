def solution(scores):
    # 각 학생의 평균을 계산하여 (평균, 학생 번호)의 튜플로 구성된 리스트 생성
    averages = [(sum(score) / len(score), idx) for idx, score in enumerate(scores)]
    
    # 평균을 기준으로 내림차순 정렬
    sorted_averages = sorted(averages, key=lambda x: x[0], reverse=True)
    
    # 등수를 구해서 결과 리스트에 저장
    result = [0] * len(scores)
    rank = 0
    prev_avg = None
    
    for i, (avg, idx) in enumerate(sorted_averages):
        if avg != prev_avg:
            rank = i + 1
        result[idx] = rank
        prev_avg = avg
    
    return result