def solution(n, costs):
    # kruskal algorithm
    costs.sort(key = lambda x: x[2]) #그리디하게 cost 작은것부터 연결
    routes = set([costs[0][0]]) #루트노드를 시작으로 n-1개의 간선을 연결
    minCost = 0
    
    while len(routes) < n :
        for i,cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes: #간선 연결
                routes.update([cost[0],cost[1]])
                minCost += cost[2]
                costs[i] = [-1,-1,-1] #이미 연결한 것은 다시 연결안하도록 
                break
                
    return minCost
