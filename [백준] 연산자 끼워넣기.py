minValue = 1000000000
maxValue = -1000000000


def dfs(depth,total):
    global minValue,maxValue
    global numbers,n,operators
    if depth == n:
        minValue = min(total,minValue)
        maxValue = max(total,maxValue)
        return

    #+,-,x,/
    if operators['+'] > 0 :
        operators['+'] -= 1
        dfs(depth+1,total + numbers[depth])
        operators['+'] += 1

    if operators['-'] > 0 :
        operators['-'] -= 1
        dfs(depth+1,total - numbers[depth])
        operators['-'] += 1

    if operators['*'] > 0 :
        operators['*'] -= 1
        dfs(depth+1,total * numbers[depth])
        operators['*'] += 1

    if operators['/'] > 0 :
        operators['/'] -= 1
        next_total = 0 if total == 0 else ((abs(total) // total) * (abs(total) // numbers[depth]))
        dfs(depth+1,next_total)
        operators['/'] += 1
    



if __name__=='__main__':
    n = int(input())
    numbers = list(map(int,input().split()))
    counts = list(map(int,input().split()))
    operators = {}
    for oper,count in zip(['+','-','*','/'],counts):
        operators[oper] = count

    dfs(1,numbers[0])
    print(maxValue)
    print(minValue)
