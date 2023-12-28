def solution(nums):
    nums.sort()
    answer = max(nums[0] * nums[1], nums[-1] * nums[-2])

    return answer