def solution(numbers, target):
    def dfs(index=0, current_sum=0):
        # 1. 탈출 조건: 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            if current_sum == target:
                return 1    # 타겟 완성
            else: 
                return 0    # 실패


        # 2. 수행 동작: 현재 숫자를 더하는 경우와 빼는 경우
        return dfs(index+1, current_sum+numbers[index]) + \
                dfs(index+1, current_sum-numbers[index])

    return dfs()