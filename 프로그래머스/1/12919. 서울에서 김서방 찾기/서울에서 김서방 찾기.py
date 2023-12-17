def solution(seoul):
    for firstname in seoul:
        if 'Kim' == firstname:
            return f'김서방은 {seoul.index(firstname)}에 있다'