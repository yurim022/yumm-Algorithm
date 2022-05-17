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


--------
  
    # 괜찮았던 풀이 -> 시간복잡도 이게 더 굿. 
    # map을 두번 초기화 하지 않았고, 위에는 while문에 매번 if문 체크와 pre/cur, changed가 반복 연산되던것을 스택을 통해 한번에 연산했다. 
    
    def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer
