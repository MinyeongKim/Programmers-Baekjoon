def solution(name, yearning, photo):
    name_grade = {} #이름, 점수 쌍
    answer = []
    
    for i, j in zip(name, yearning) :
        name_grade[i] = j
    
    for i in range(len(photo)):
        answer.append(0) #배열 초기화
        for j in photo[i]:
            if j in name_grade:
                answer[i] += name_grade[j]

    
    
    return answer