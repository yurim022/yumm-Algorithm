from collections import defaultdict
from collections import deque
def solution(n, edge):
    graph = [ [] for i in range(n+1)]
    distance = defaultdict(list)
    visited = [False] * (n+1)

    for e1,e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    q = deque([(1,0)]) # 1번 노드부터 시작
    visited[1] = True

    while q:
        prev, prev_depth = q.popleft()
        depth = prev_depth + 1
        for cur in graph[prev]:
            if not visited[cur]:
                visited[cur] = True
                distance[depth].append(cur)
                q.append((cur,depth))
                
    far = max(distance.keys())
    return len(distance[far])
