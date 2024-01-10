def solution(wallpaper):
    #드래그 시작점과 끝점
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if lux > i: lux = i
                if luy > j: luy = j
                if rdx < i+1: rdx = i+1
                if rdy < j+1: rdy = j+1
    
    
    answer = []
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    
    return answer