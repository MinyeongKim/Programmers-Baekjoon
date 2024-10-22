def solution(k, tangerine):
    answer = 0
    num = {}
    
    for i in tangerine:
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
            
    num = sorted(num.values(), reverse=True)
    
    for i in num:
        answer += 1
        k -= i
        if k<=0:
            break
    
    return answer