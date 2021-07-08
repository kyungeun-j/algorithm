from operator import itemgetter
def solution(strings, n):
    return [i[0] for i in sorted([(j, j[n]) for j in sorted(strings)], key=itemgetter(1))]