n = int(input())
cnt = 0
point = []

def dfs(col):
    global cnt, point
    if col == n:
        cnt += 1
        return

    for i in range(1,n+1):
        if valid(i,col+1):
            point.append([i,col+1])
            dfs(col+1)
            point.pop()


def valid(row,col):
    global point
    for p in point:
        queen_r , queen_c = p[0],p[1]
        if row == queen_r or abs(queen_c - col) == abs(queen_r - row):
            return False

    return True


    

if __name__=='__main__':
    dfs(0)
    print(cnt)
    
    
    #col 인덱스를 0부터 시작하는게 차라리 더 깔끔했을 거 같다
    
    ----------------------------------
    
    #다른 코드 -> 이게 더 효율적이당
    
    
    n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == (x -i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    for i in range(n):
        row[x] = i
        if is_promising(x):
            n_queens(x+1)

if __name__=='__main__':
    n_queens(0)
    print(ans)
