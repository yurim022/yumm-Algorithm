import java.util.*;
class Solution {
     // floyd  완전탐색 
        static final int INF = 100000*200; 
        int[][] dist = new int[201][201]; // 각 지점 까지의 최단거리
    //floyd
        void floyd(int n) {
            for(int midPoint = 1; midPoint <= n; ++midPoint){
                for(int start = 1; start <= n; ++start ){
                    for(int end = 1; end <= n; ++end){
                        if(dist[start][end] > dist[start][midPoint] + dist[midPoint][end]){
                            dist[start][end] = dist[start][midPoint] + dist[midPoint][end];
                         }
                    }  
                }
            }
        }
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        
        int answer = INF;
        
        for(int i = 1; i<= n; ++i)
            for(int j = 1; j <= n; ++j){
                if(i==j)
                    dist[i][j] = 0;
                if(i!=j)
                    dist[i][j] = INF;
            }
                   
        for(int[] fare : fares){
            dist[fare[0]][fare[1]] = fare[2];
            dist[fare[1]][fare[0]] = fare[2];
        }
        
        floyd(n);
        
        //완전탐색
        for(int node = 1; node <= n; ++node){
            answer = Math.min(answer,dist[s][node]+dist[node][a]+dist[node][b]);
        }
        
        return answer;
    }
}
