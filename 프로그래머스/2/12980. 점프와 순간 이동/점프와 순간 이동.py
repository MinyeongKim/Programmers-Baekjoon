def solution(n):
    ans = 0
    energy = 0
    
    #순간이동은 무조건 지금까지 온 거리 2배
    
    while True:
        if n == 0:
            break
        
        if n % 2  == 0:
            n /= 2
        else:
            n -= 1
            energy += 1
    
    return energy