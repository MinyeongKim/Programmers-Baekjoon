def solution(clothes):
    answer = 1
    clothe = {}
    
    for i, j in clothes:
        if j in clothe.keys():
            clothe[j] += 1
        else:
            clothe[j] = 2
    
    for i in clothe.values():
        answer *= i
    
    answer -= 1
    
    return answer