def solution(price):
    if price >= 10**5:
        if price >= 3*(10**5):
            if price >= 5*(10**5):
                return int(price*0.8)
            return int(price*0.9)
        return int(price*0.95)
    return price