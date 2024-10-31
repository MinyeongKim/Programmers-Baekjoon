def solution(s):
    answer = []
    
    #문자열 s 리스트로 변환
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    t = eval(s)
    
    t = sorted(t, key=len)
    
    for i in t:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer