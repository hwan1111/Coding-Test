def solution(nums):
    answer = min(len(nums) // 2, len(set(nums))) - 1
    
    return answer + 1