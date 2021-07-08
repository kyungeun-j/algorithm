def solution(arr, divisor):
    a = [i for i in arr if i % divisor == 0]
    
    return sorted(a) if len(a) != 0 else [-1]