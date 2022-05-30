import copy
def solution(triangle):
    global max_value
    max_value = copy.deepcopy(triangle)
    for depth in range(1,len(triangle)):
        dp(depth)
    
    return max(max_value[len(triangle)-1])


def dp(depth):
    max_value[depth][0] += max_value[depth-1][0]
    for i in range(1,depth):
        max_value[depth][i] = max_value[depth][i] + max(max_value[depth-1][i-1],max_value[depth-1][i])
    max_value[depth][depth] += max_value[depth-1][depth-1]
