dx = [1,0,-1,0]
dy = [0,-1,0,1]

def solution(grid):
    #시뮬레이션
    global visited,n,m
    n = len(grid)
    m = len(grid[0])
    visited = [ [[False]*4 for _ in range(m) ] for _ in range(n)] #방향까지 visited로 설정
    answer = []
    for sx in range(n):
        for sy in range(m):
            for sd in range(4):
                if not visited[sx][sy][sd]:
                    path_len = simul(sx,sy,sd,grid)
                    if path_len != 0 :
                        answer.append(path_len)
    
    answer.sort()
    return answer


def simul(sx,sy,sd,grid):
    visited[sx][sy][sd] = True
    x,y,d = sx,sy,sd
    path_len = 0
    
    while True:
        #이동
        x = (x + dx[d])%n
        y = (y + dy[d])%m
        if grid[x][y] == 'R':
            d = (d+1)%4
        elif grid[x][y] == 'L':
            d = (d-1)%4
        
        path_len += 1
        
        #이미 방문했던 경로
        if visited[x][y][d]:
            if (x,y,d) == (sx,sy,sd):
                return path_len
            return 0
        
        visited[x][y][d] = True
