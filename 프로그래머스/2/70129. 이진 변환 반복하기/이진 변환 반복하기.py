def solution(s):
    cnt = 0
    z_num = 0
    x = s

    
    while x != "1":        
        cnt = cnt + 1
        z_num = z_num + x.count('0')
        x = bin(len(x)-x.count('0'))[2:]
    
    
    answer = [cnt, z_num]    
    return answer