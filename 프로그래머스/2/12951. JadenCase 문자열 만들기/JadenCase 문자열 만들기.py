def solution(s):
    l = list(s.split(" "))
    
    print(l)
    for i in range(len(l)):
        l[i] = l[i].capitalize()
        
    answer = ' '.join(l)
    
    return answer