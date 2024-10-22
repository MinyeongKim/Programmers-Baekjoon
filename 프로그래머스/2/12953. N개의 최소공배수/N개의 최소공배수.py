import math

def solution(arr):
    answer = arr[0]
    
    if len(arr) == 1:
        return answer
    
    for i in arr[1:]:
        temp = answer * i // math.gcd(answer, i)
        answer = temp
        
    
    return answer