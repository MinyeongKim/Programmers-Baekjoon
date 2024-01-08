def solution(park, routes):
    answer = []
    height = len(park)
    width = len(park[0])
    x = 0 #시작 위치 x좌표
    y = 0 #시작 위치 y좌표
    flag = 0
    
    #시작 위치 찾기
    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                x = i
                y = j
                flag = 1
                break
        if flag == 1:
            break
    
    #산책
    mx = x #현재 x좌표
    my = y #현재 y좌표
    
    for route in routes:
        way = route.split()
        if way[0] == 'N':
                 for step in range(1, int(way[1])+1):
                    if (mx-step < 0) or park[mx-step][my] =='X':
                        break
                    elif step == int(way[1]):
                        mx = mx - step

        elif way[0] == 'S':
            for step in range(1, int(way[1])+1):
                if (mx+step > height-1) or (park[mx+step][my] == 'X'):
                    break
                elif step == int(way[1]):
                    mx = mx + step
        elif way[0] == 'W':
            for step in range(1, int(way[1])+1):
                if (my-step < 0) or park[mx][my-step] =='X':
                    break
                elif step == int(way[1]):
                        my = my - step
        elif way[0] == 'E':
            for step in range(1, int(way[1])+1):
                if (my+step > width-1) or park[mx][my+step] =='X':
                    break
                elif step == int(way[1]):
                    my = my + step
    
    answer.append(mx)
    answer.append(my)
    
    return answer