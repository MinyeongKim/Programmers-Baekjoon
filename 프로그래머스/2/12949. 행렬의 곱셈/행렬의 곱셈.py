def solution(arr1, arr2):    
    A = len(arr1)
    B = len(arr1[0])
    C = len(arr2[0])
    
    answer = [[0]*C for i in range(A)]
    
    
    for i in range(A):
        for j in range(C):
            answer[i][j] = sum([arr1[i][k]*arr2[k][j] for k in range(B)])
    
    return answer