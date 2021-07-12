import math
def solution(left, right):
    return sum([i  if int(math.sqrt(i)) != math.sqrt(i) else -i for i in range(left, right+1)])