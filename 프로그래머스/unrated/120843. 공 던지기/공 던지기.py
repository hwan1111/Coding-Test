def solution(nums, k):
    return nums[2*(k-1) % len(nums)]