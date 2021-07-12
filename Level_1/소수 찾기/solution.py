def solution(n):
    a = list(range(2, n+1))
    b = []
    for i in list(range(0, len(a))):
        b += a[i::a[i]][1::]     
    return n-1-len(set(b))