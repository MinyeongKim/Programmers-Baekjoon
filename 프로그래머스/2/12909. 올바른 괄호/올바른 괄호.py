def solution(s):
    l = 0
    
    for i in s:
        if l < 0: break;
        elif i == '(': l = l+1
        elif i == ')': l = l-1
        
    if l == 0 : answer = True
    else: answer = False

    return answer