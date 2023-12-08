#2587, 대표값 2
#5개의 수의 평균과 중앙값을 구하는 문제

nums = []
for i in range(5):
    nums.append(int(input()))

nums.sort()
print(int(sum(nums)/5))
print(nums[2])