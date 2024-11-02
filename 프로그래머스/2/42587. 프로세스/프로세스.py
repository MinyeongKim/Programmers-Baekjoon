def solution(priorities, location):
    answer = 0
    que = [(i,j) for i,j in enumerate(priorities)]
    
    while len(que) != 0:
        top = que.pop(0)
        
        if any(top[1] < q[1] for q in que):
            que.append(top)
        else:
            answer += 1
            if top[0] == location:
                return answer

    return answer