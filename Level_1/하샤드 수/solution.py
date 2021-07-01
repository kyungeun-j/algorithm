def solution(x):
    
    xSum = sum(int(i) for i in str(x))
    answer = True if x%xSum==0 else False
    
    return answer