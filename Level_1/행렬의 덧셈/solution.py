def solution(arr1, arr2):
    answer = [ [ i+j for i,j in zip(arr1[x], arr2[x]) ] for x in range(len(arr1)) ]
    return answer