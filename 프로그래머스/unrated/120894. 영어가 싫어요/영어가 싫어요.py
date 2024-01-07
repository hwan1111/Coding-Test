def solution(nums):
    En_to_num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
                  'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = ''
    num = ''
    for i in nums:
        num += i
        if num in En_to_num:
            answer += En_to_num[num]
            num = ''
    
    return int(answer)