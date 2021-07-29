def solution(n):
    n3 = ''
    
    while n > 0:
        n, m = divmod(n, 3)
        n3 += str(m)
    
    return int(n3, 3)