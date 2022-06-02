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
    
    
    
    
    
    
    
    
    
    ----------------------------------
    
    #다른 코드 -> 이게 더 효율적이당
    
    
    
