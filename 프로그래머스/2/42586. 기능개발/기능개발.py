def solution(progresses, speeds):
    answer = []
    days = []
    for i in progresses:
        days.append(100 - i)
        
    for j in range(len(speeds)):
        if days[j] % speeds[j] == 0:
            days[j] = days[j] // speeds[j]
        else:
            days[j] = days[j] // speeds[j] + 1
    
    temp = 1
    max_d = days[0]
    for k in range(1, len(days)):
        if days[k] > max_d:
            max_d = days[k]
            answer.append(temp)
            temp = 1
        else:
            temp += 1
    answer.append(temp)
    
    return answer