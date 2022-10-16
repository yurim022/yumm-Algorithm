def solution(n):
    global answer
    answer = []
    def dfs(depth,start,passBy,destination):
        global answer
        if depth == 1:
            answer.append([start,destination])
            return
            
        dfs(depth-1,start,destination,passBy) #목적지 옆에 n-1개 쌓기
        
        answer.append([start,destination]) #맨 밑에 있는 것 목적지로 옮기기
        
        dfs(depth-1,passBy,start,destination) # 목적지 옆에 쌓아뒀던 것 다시 옮기기
        
        
    dfs(n,1,2,3)
    return answer
