package programmers;

import java.util.*;
class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        Queue<Integer> rotate = new LinkedList<>();
        int[] answer = new int[queries.length];
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        
        int[][] graph = new int[(rows+1)][(columns+1)];
        int number = 1;
        for(int row = 1; row <= rows; row++){
            for(int col = 1; col <= columns; col++){
                graph[row][col] = number;
                number++;
            }
        }
        
        for(int i = 0; i < queries.length; i++){
            
            int x1 = queries[i][0];
            int y1 = queries[i][1];
            int x2 = queries[i][2];
            int y2 = queries[i][3];
            
            int x = x1;
            int y = y1;
            int nx = 0; //임시값 저장을 위해
            int ny = 0;
            rotate.add(graph[x][y]);
            for(int dir = 0; dir <4; dir++){ 
                while(true){
                    nx = x + dx[dir];
                    ny = y + dy[dir];
                    
                    if(nx < x1 || nx > x2 || ny < y1 || ny > y2)
                        break;
                    if(dir == 3 && nx == x1 && ny == y1) //맨 마지막은 중복되니까 제외
                        break;
                    x = nx;
                    y = ny;
                    rotate.add(graph[x][y]); //이게 맨 마지막에 와야함 주의! 안그러면 경계값에서 두번 들어갈 수 있음
                }
            }
            
            answer[i] = rotate.stream().mapToInt(v -> v).min()
                .orElseThrow(NoSuchElementException::new); //최소값
            
            //배열 rotate
            
            x = x1;
            y = y1;
            for(int dir = 0; dir <4; dir++){ 
                while(true){
                    nx = x + dx[dir];
                    ny = y + dy[dir];
                    
                    if(nx < x1 || nx > x2 || ny < y1 || ny > y2)
                        break;
                    
                    x = nx;
                    y = ny;
                    
                    graph[x][y] = rotate.poll();
                }
            }
            
        }
        
        return answer;
    }
}
