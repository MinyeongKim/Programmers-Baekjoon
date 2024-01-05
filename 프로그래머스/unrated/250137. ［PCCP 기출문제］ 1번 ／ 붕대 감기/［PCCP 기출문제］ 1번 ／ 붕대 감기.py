def solution(bandage, health, attacks):
    current_health = health
    max_time = attacks[-1][0]
    t = bandage[0] #기술의 시전시간
    x = bandage[1] #1초당 회복량
    y = bandage[2] #추가회복량
    current_t = 0 #현재 시간
    c_t = 0 #연속 회복 시간
    
    attack_t = {}
    for i in attacks:
        attack_t[i[0]] = i[1]
    
    while current_t <= max_time:
        if current_t in attack_t:
            current_health = current_health - attack_t[current_t]
            c_t = 0
            if current_health <= 0:
                return -1
            
        else:
            current_health = current_health + x
            c_t = c_t+1
            
            if c_t == t:
                current_health = current_health + y
                c_t = 0
                
            if current_health > health:
                    current_health = health

        
        current_t = current_t+1
        
    return current_health