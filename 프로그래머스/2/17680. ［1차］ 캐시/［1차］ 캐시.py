from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city) 
            cache.appendleft(city)
            answer += 1
        else:
            # Cache Miss: 맨 앞에 추가하고 사이즈 초과 시 가장 오래된 뒤쪽 제거
            answer += 5
            cache.appendleft(city)
            if len(cache) > cacheSize:
                cache.pop()
                
    return answer