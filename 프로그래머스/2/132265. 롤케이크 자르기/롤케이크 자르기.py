from collections import Counter

def solution(topping):
    # 1. 처음에는 전부 오른쪽
    right_count = Counter(topping)
    right_kind = len(right_count)
    
    left_seen = set()
    left_kind = 0
    
    answer = 0
    
    # 2. 왼쪽으로 하나씩 넘겨보기
    for t in topping:
        # t를 왼쪽에게 줌
        if t not in left_seen:
            left_seen.add(t)
            left_kind += 1
        
        # 오른쪽에는 t가 하나 줄어듦
        right_count[t] -= 1
        if right_count[t] == 0:
            right_kind -= 1
        
        # 3. 이 시점에서 둘이 같으면 공평하게 나뉜 상태
        if left_kind == right_kind:
            answer += 1
    
    return answer