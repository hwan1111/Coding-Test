# 1. ICN에서 출발하는 항공편이 여러 개라면 tickets[0][i] 가 알파벳 순서로 정렬되어야 함.
# 2. 루트노드는 무조건 'ICN'
# 3. 깊이우선으로 간다.
# 4. 공항 수가 10,000개 이기 때문에 O(N^2)이면 못푼다.

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    
    visited = [False] * len(tickets)
    
    def dfs(now, path):
        if len(path) == len(tickets) + 1:
            return path
        
        # 순회하며 다음 목적지 찾기
        for idx, ticket in enumerate(tickets):
            # 아직 안 쓴 티켓, 출발지가 현재 위치
            if visited[idx] is False and ticket[0] == now:
                visited[idx] = True
            
                # 다음 공항으로 이동
                result = dfs(ticket[1], path + [ticket[1]])
                
                # 만약 이 길로 가서 정답을 찾았다면 그대로 반환
                if result:
                    return result
                
                # 정답을 못찾았다면 막다른길, 티켓 사용 취소
                visited[idx] = False
        
        return None

    return dfs('ICN', ['ICN'])