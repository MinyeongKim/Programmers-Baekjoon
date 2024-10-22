def solution(n):
    answer = []
    
    for i in range(n+1):
        if (i == 0) or (i == 1):
            answer.append(1)
        else:
            answer.append(answer[i-1] + answer[i-2])
            
    return answer[n] % 1234567