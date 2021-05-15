from heapq import heappop,heappush
#heapq는 일반적인 리스트를 min heap처럼 다룰 수 있게 해

INF = int(1e9)
graph = [[]]

def preprocess(n,fares):
    global graph
    graph = [[] for i in range(n+1)]
    
    for fare in fares:
        src,dst,cost = fare[0],fare[1],fare[2]
        graph[src].append([dst,cost])
        graph[dst].append([src,cost])
        
def dijkstra(src,dst):
    global graph
    n = len(graph)
    table = [INF for i in range(n)] #출발지점에서 도착지점까지의 최소거리
    table[src] = 0 
    pq = [[0,src]] #COST, NODE
    
    while pq: #더이상 최솟값 갱신이 안될때까지
        c ,x= heappop(pq) #최소값 꺼내기
        
        if table[x] < c: continue #테이블에 있는 값이 더 작으면 패스.
            
        for item in graph[x]:#x node와 연결점이 있는 것 탐색
            nx, ncost = item[0],item[1]
            ncost += c
            if ncost < table[nx] : # x노드를 통해서 이동한 값이 더 작으면 갱신
                table[nx] = ncost
                heappush(pq, [ncost,nx])
                
    return table[dst]
    


def solution(n, s, a, b, fares):
    preprocess(n,fares)
    cost = INF
    
    #A,B가 헤어지는 지점을 i라고 하면, 
    #요금 = dijkstra(출발점,K)+dijkstra(K,A도착점)+dijkstra(K,B의 도착점)
    for i in range(1,n+1):
        cost = min(cost,dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))
        
    return cost










#참고할만한 풀이 
-----------------------------------------------------


from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n+1):
        Q = [(0, i)]
        visited = [True] * (n+1)
        dp = [float('inf')] * (n+1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if visited[des]:
                visited[des] = False
                for cost, destination in dic[des]:
                    dp[destination] = min(cost + dp[des], dp[destination])
                    heapq.heappush(Q, (dp[destination], destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)
