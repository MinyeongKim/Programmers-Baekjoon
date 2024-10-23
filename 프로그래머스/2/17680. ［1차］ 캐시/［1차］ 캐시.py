def solution(cacheSize, cities):
    answer = 0
    cache = []
    top = 0
    
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        city = i.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        elif top < cacheSize:
            answer += 5
            top += 1
            cache.append(city)
        else:
            answer += 5
            cache.pop(0)
            cache.append(city)
        
    return answer