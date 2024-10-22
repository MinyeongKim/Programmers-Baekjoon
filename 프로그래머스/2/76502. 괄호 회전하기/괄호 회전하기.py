def solution(s):
    answer = 0
    arr = []
    
    for i in range(len(s)):
        for j in s:
            if len(arr) == 0:
                arr.append(j)
            elif j == ']' and arr[-1] == '[':
                    arr.pop()
            elif j == ')' and arr[-1] == '(':
                    arr.pop()
            elif j == '}' and arr[-1] == '{':
                    arr.pop()
            else:
                arr.append(j)
        
        
        if len(arr) == 0:
            answer += 1
        
        arr = []        
        s = s[1:] + s[0]
    
    return answer