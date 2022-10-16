def solution(m, n, puddles):

    route = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    route[1][0] = 1 #최단경로 배열
    for x,y in puddles:
        route[y][x] = -1
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            if route[i][j] == -1:
                route[i][j] = 0
                continue
            route[i][j] = route[i-1][j] + route[i][j-1] #dp
            
    return route[n][m] % 1000000007
