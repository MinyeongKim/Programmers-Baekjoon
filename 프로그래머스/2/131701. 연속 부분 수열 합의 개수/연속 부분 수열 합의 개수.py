def solution(elements):
    answer = set([])
    a, b = 0, 0
    len_e = len(elements)
    elements = elements*2
    
    for i in range(0, len_e):
        a = 0
        b = i
        
        for j in range(len_e):
            answer.add(sum(elements[a:b+1]))
            a += 1
            b += 1
    
    return len(answer)