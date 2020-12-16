from itertools import product

def solution(numbers, target):
    l = [(x,-x) for x in numbers]
    s = list(map(sum,product(*l)))
    return s.count(target)

#원래 의도에 맞게 DFS
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:],target+numbers[0])+ solution(numbers[1:],target-numbers[0])
