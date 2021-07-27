def solution(d, budget):    
    d = sorted(d, reverse=True)
    
    while budget < sum(d):
        del d[0]
        
    return len(d)