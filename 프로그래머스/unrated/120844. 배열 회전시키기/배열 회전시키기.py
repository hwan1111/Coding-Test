def solution(nums, direc):
    
    if direc == 'right':
        el = nums.pop()
        return [el] + nums
    else:
        el = nums.pop(0)
        return nums+[el]