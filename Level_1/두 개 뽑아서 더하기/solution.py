def solution(numbers):
    return sorted(list(set([numbers[i]+j for i in range(len(numbers)) for j in numbers[i+1::]])))