from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for p in permutations(dungeons):
        total = k
        cnt = 0
        
        for need_k, use_k in p:
            if need_k <= total:
                total -= use_k
                cnt += 1
        
        answer.append(cnt)
    
    return max(answer)