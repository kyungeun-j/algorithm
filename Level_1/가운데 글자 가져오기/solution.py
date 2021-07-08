def solution(s):
    return s[(len(s)-1)//2]+s[(len(s)-1)//2+1] if len(s) % 2 == 0 else s[(len(s)-1)//2]