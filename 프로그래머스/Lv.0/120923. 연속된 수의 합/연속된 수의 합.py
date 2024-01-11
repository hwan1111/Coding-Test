def solution(num, total):
    median = total // num

    return [i for i in range(median - (num-1)//2, median + (num + 2)//2)]


