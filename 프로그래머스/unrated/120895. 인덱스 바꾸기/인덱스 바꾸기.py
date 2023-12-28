def solution(my_str, num1, num2):
    front = my_str[:num1]
    mid = my_str[num1+1:num2]
    back = my_str[num2+1:]

    return front+my_str[num2]+mid+my_str[num1]+back