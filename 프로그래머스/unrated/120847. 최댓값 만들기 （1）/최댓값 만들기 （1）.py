def solution(nums):
    nums = sorted(nums, reverse=True)
    return nums[0]*nums[1]