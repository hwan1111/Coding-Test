from collections import deque

def solution(priorities, location):
    # 프로세스와 원래 위치를 쌍으로 큐에 저장
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    execution_order = 0  # 실행 순서 카운트
    
    while queue:
        # 큐에서 첫 번째 프로세스 꺼내기
        current = queue.popleft()
        
        # 우선순위가 더 높은 프로세스가 있다면 다시 큐의 뒤로 이동
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            # 현재 프로세스 실행
            execution_order += 1
            # 만약 현재 프로세스가 우리가 찾는 위치의 프로세스라면 실행 순서 반환
            if current[1] == location:
                return execution_order
