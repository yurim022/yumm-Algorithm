dx = [0,1,0,-1] #시계방향
dy = [1,0,-1,0]

def solution(rows, columns, queries):
    answer = []
    maps = [[0] * (columns+1) for _ in range(rows+1)]
    num = 1
    for i in range(1, rows+1): #map 초기화
        for j in range(1, columns+1):
            maps[i][j] = num
            num += 1
            
    for q in queries:
        x1, y1, x2, y2 = q
        pre = maps[x1][y1]
        x,y = x1, y1
        changed = []
        for d in range(4):
            while True:
                x += dx[d]
                y += dy[d]
                changed.append(pre)
                cur = maps[x][y]
                maps[x][y] = pre
                pre = cur
                #모서리면
                if (x,y) in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
                    break
        answer.append(min(changed))
        
    return answer
