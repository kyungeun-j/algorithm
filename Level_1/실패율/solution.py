def solution(N, stages):
    sP = [stages.count(i) for i in range(1, N+2)]
    cP = [sum(sP[j:]) for j in range(len(sP))]
    per = [0 if i == 0 else i/j for i,j in zip(sP, cP)]
    
    return [n for p, n in sorted(zip(per, range(1, N+1)), key = lambda x: x[0], reverse = True)]