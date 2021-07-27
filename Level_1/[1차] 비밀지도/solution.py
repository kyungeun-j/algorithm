def solution(n, arr1, arr2):
    return [format(i|j, 'b').replace('1', '#').replace('0', ' ').rjust(n, ' ') for i,j in zip(arr1, arr2)]