def solution(n, m):
    answer = []
    
    a = max(n,m)
    b = min(n,m)
    
    while b != 0:
        re = a%b
        a = b
        b = re
        
    answer = [a, n*m/a]
    
    return answer