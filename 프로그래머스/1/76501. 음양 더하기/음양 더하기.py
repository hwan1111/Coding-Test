def solution(absolutes, signs):
    real_num = [absolutes[i] if signs[i] is True else -(absolutes[i]) for i in range(len(absolutes))]
    return sum(real_num)