def solution(n):
    
    answer = 0
    n_1 = (bin(n)[2:]).count('1')
    
    
    while True:
        n += 1
        if n_1 == (bin(n)[2:]).count('1'):
            answer = n
            break
    
    return answer