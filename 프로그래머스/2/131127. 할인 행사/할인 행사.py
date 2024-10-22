def solution(want, number, discount):
    answer = 0
    
    
    for i in range(len(discount)-9):
        want_list = dict(zip(want, number))
        
        for j in discount[i:10+i]:
            if j in want and want_list[j] != 0:
                want_list[j] -= 1
        
        if sum(want_list.values()) == 0:
            answer += 1
    
    return answer