def solution(s):

    answer = ''
    s = s.split(' ')
    for i, z in enumerate(s):
        answer += ''.join([k.upper() if j%2==0 else k.lower() for j,k in enumerate(z)])
        if i < len(s)-1:
            answer += ' '
            
    return answer