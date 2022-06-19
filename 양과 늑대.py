def solution(info, edges):
    childs = {}
    for i in range(len(info)):
        childs[i] = []
    for parent,child in edges:
        childs[parent].append(child)
        
    def dfs(current,path,sheep,wolf):
        if info[current]:
            wolf += 1
        else:
            sheep += 1
        
        # 늑대수가 양보다 많거나 같으면 끝
        if sheep <= wolf:
            return 0
        
        maxSheep = sheep # for문 밖에 선언해줘야함 주의!
        for p in path: # 다시 올라갈 수 있으므로 path 처음부터 다시 둘러봄
            for nextNode in childs[p]:
                if nextNode not in path:
                    path.append(nextNode)
                    maxSheep = max(maxSheep,dfs(nextNode,path,sheep,wolf)) 
                    path.pop()
                    
        return maxSheep
    
    return dfs(0,[0],0,0)
