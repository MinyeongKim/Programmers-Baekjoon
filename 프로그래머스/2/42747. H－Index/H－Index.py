def solution(citations):
    answer = 0
    
    cnt = 0
    citations = sorted(citations, reverse=True)
    
    for i in citations:
        cnt += 1
        
        if cnt <= i:
            answer = cnt
    
    return answer