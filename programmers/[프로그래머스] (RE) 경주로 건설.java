package programmers;

import java.util.*;

/*
if 만으로 나타내는것 가독성 좋지만 실수발생 할 수 있음
if( (dir == -1) || (dir == nDir)){
                    nCost += 100;
                } //처음시작, 직선
if(dir != nDir){
                    nCost += 600;
                }//코너
                

이렇게 하면 -1인경우에 다 더해져서 오류생김!
if(dir != -1 && dir != nDir) 
*/
class Solution {

    private static int n;
    private static int[] dx = {-1,0,1,0}; //상우하좌 
    private static int[] dy = {0,1,0,-1};
    private static int minValue = Integer.MAX_VALUE;
    private static boolean[][] visited;//boolean은 초기값 false
    private static int[][] map;
    
    public int solution(int[][] board) {
    
        n = board.length;
        map = board;
        visited = new boolean[n][n];
        bfs();
        
        return minValue;
    
    }
    
    private static void bfs(){
        Queue<Road> roadQ = new LinkedList<>();
        roadQ.add(new Road(0,0,-1,0));
        visited[0][0] = true;
        
        while(!roadQ.isEmpty()){
            Road road = roadQ.remove();
        
            int x = road.x;
            int y = road.y;
            int dir = road.dir;
            int cost = road.cost;

            if(x == n-1 && y == n-1){
                minValue = Math.min(minValue,cost);
            }

            for (int i = 0 ; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nDir = i; 
                int nCost = cost; //cost여기서 다시 정의해주는 것 주의! 

                if (nx < 0 || nx >= n || ny < 0 || ny >= n || map[nx][ny] == 1 ) //범위를 벗어났거나 벽
                    continue;

                if( (dir == -1) || (dir == nDir)){
                    nCost += 100;
                } //처음시작, 직선
                else {
                    nCost += 600;
                }//코너



                if( !visited[nx][ny] || map[nx][ny] >= nCost){
                    visited[nx][ny] = true;
                    map[nx][ny] = nCost;
                    roadQ.add(new Road(nx,ny,nDir,nCost));
                }

            }//for문 종료
            
        }
          
        
    }
    
    
}
class Road {
        int x;
        int y;
        int dir;
        int cost;
        
        Road(int x, int y, int dir,int cost){
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.cost = cost;
        }
}
