def solution(my_str):
    nums = []
    for char in my_str:
        if char.isdigit():
            nums.append(int(char))
    
    return sum(nums)