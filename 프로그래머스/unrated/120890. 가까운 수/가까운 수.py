def solution(array, n):
    answer = array[0]
    min_difference = abs(array[0] - n)

    for num in array:
        difference = abs(num - n)

        if difference < min_difference or (difference == min_difference and num < answer):
            min_difference = difference
            answer = num
    
    return answer