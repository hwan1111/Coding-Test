import sys

def solve():
    # 문제의 조건: k와 n은 1 이상 14 이하
    # answer[k][n]을 저장할 2차원 배열 (15x15 크기)
    # answer[층][호]
    answer = [[0] * 15 for _ in range(15)]
    
    # 기저 상태 (Base Case) 설정
    for i in range(1, 15):
        answer[0][i] = i    # 0층의 i호에는 i명이 산다
        answer[i][1] = 1    # i층의 1호에는 항상 1명이 산다
    
    # 점화식을 이용한 answer 테이블 채우기
    # answer[k][n] = answer[k][n-1] (옆집)+ answer[k-1][n] (아랫집)
    for k in range(1, 15):
        for n in range(2, 15):
            answer[k][n] = answer[k][n-1] + answer[k-1][n]
            
    return answer

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    answer = solve()
    for _ in range(T):
        k = int(sys.stdin.readline().strip())
        n = int(sys.stdin.readline().strip())
        print(answer[k][n])