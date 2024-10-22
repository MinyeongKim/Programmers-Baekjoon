def solution(brown, yellow):
    y_w = []
    y_h = []
    w, h = 0, 0
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_w.append(i)
            y_h.append(int(yellow / i))
    
    for j in range(len(y_w)):
        if (y_w[j] + 2) * (y_h[j] + 2) - yellow == brown:
            w = y_w[j] + 2
            h = y_h[j] + 2
    
    answer = [w, h]
    
    return answer