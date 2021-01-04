//틀린코드...
//반례. 이미 연결관계를 가진 것은 추가 할 필요 없음

import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0, curr = 0;
        
        //비용이 적은 순서대로 정렬
        Arrays.sort(costs, new Comparator<int[]>(){
            @Override
            public int compare(int[] t1,int[] t2){
                return t1[2]-t2[2];
            }
        });
        
        int[][] link = new int[n][n]; //연결관계
        
        do{
            int node1 = costs[curr][0], node2 = costs[curr][1], cost = costs[curr][2];
            answer += cost;
            curr += 1;
            link[node1][node2] = link[node2][node1] =1;
           //String a = Integer.toString(node1);
           //String b = Integer.toString(node2);
           //System.out.println(a+" "+b);
        }while(validate(n,link));
        
        //for(int[] arr:costs){
          //  System.out.println(Arrays.toString(arr));
        //}
        return answer;
    }
    
    public boolean validate(int n, int [][] link){
        boolean[] visited = new boolean[n];
        Arrays.fill(visited,false);
        
        //BFS
        int root = 0, count = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(root);
        visited[root] =true;
        while(!q.isEmpty()){
            int e = q.poll();
            for(int i = 0; i<n;i++){
                if (!visited[i] && link[i][e] == 1){
                    count += 1;
                    q.add(i);
                    visited[i] =true;
                }
            }
        }
        
        if (count == n){return false;}
        return true;
        
    } 
}
