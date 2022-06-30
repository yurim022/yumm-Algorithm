def solution(n):
    maps = [ [0]*(i+1) for i in range(n)]
    move = [(1,0),(0,1),(-1,-1)] #행,열 방향
    direction = 0 #0,1,2
    
    
    finalNum = n*(n+1)//2
    num = 1
    cur_r,cur_c = 0,0
    maps[0][0] = 1 #끝에값 조심!!!!
    while finalNum > num:
        next_r, next_c = cur_r + move[direction][0], cur_c + move[direction][1]
        if next_r < n and next_c < n and next_r >= 0 and next_c >= 0 and maps[next_r][next_c] == 0:
            num += 1
            cur_c, cur_r = next_c, next_r
            maps[cur_r][cur_c] = num
        else:
            direction = (direction+1)%3 #범위 안에 없을 시 방향 바꾸기
        
    answer = []
    for i in range(n):
        for j in range(i+1):
            answer.append(maps[i][j])
        
    return answer
