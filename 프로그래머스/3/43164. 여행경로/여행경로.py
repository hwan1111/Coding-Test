def solution(tickets):
    # 1. 모든 티켓을 알파벳 순으로 정렬 (그래야 처음 찾은 경로가 정답이 됨)
    tickets.sort()
    
    # 티켓 사용 여부를 체크할 리스트 (원래 코드에는 없던 부분)
    visited = [False] * len(tickets)
    
    # 정답을 담을 리스트 (처음은 항상 ICN)
    answer = ['ICN']
    
    def dfs(current_airport):
        # 모든 티켓을 다 썼다면 성공! (티켓 수 + 1이 경로의 길이)
        if len(answer) == len(tickets) + 1:
            return True
        
        # 원래 코드의 index() 대신, 전체 티켓을 돌며 조건에 맞는 티켓 탐색
        for idx, ticket in enumerate(tickets):
            # 아직 안 쓴 티켓이고, 현재 공항에서 출발하는 티켓이라면
            if not visited[idx] and ticket[0] == current_airport:
                visited[idx] = True   # 티켓 사용 처리
                answer.append(ticket[1]) # 경로에 추가
                
                # 다음 목적지로 이동 (재귀)
                if dfs(ticket[1]):
                    return True # 성공하면 쭉 올라가며 종료
                
                # [중요] 여기가 백트래킹! 만약 이 길로 가서 실패했다면?
                visited[idx] = False  # 티켓 사용 취소
                answer.pop()          # 경로에서 제거
        
        return False

    # ICN에서 시작
    dfs('ICN')
    
    return answer