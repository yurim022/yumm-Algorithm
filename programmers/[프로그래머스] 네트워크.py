from collections import deque

def solution(n, computers):
    visited = [False]*n
    answer = 0
             
    def BFS(i):
        visited[i] = True
        q = deque([i])
        while q: #q가 존재하는 동안
            e = q.popleft()
            for idx in range(n):
                if computers[e][idx] == 1 and not visited[idx]:
                    visited[idx] = True
                    q.append(idx)
                    
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
    return answer    
