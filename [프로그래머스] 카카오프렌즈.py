import java.util.LinkedList;
import java.util.Queue;

#stack 사용하면 시간초과
#bfs 사용해서 풀이


class Solution {
    static int [] dx  = {1,-1,0,0,};
    static int [] dy = {0,0,1,-1};
    static int m;
    static int n;
    static int[][] picture;
    static boolean [][] visited;
    static int size;
  
  public int[] solution(int m_, int n_, int[][] picture_) {
    int numberOfArea = 0;
    int maxSizeOfOneArea = 0;
        
        m = m_;
        n = n_;
        visited = new boolean[m][n];
        picture = picture_;
      System.out.println(picture);
      
      for(int i = 0; i < m; i++){
          for(int j = 0; j<n; j++){
              if(visited[i][j] != true && picture[i][j]>0 ){
                  size = 1;
                  bfs(i,j);
                  numberOfArea++;
                  
                  if( maxSizeOfOneArea < size){
                      maxSizeOfOneArea = size;
                  }
              }
              
          }
      }
      int[] answer = new int[2];
      answer[0] = numberOfArea;
      answer[1] = maxSizeOfOneArea;
      return answer;
  }
    
    public void bfs(int y, int x){
        visited[y][x] = true;
        
        Queue<Node> q = new LinkedList<Node>();
        q.add(new Node(y,x));
        while(!q.isEmpty()){
            
            Node current = q.poll();
            
            for(int i = 0; i<4; i++){
                int ny = current.y + dy[i];
                int nx = current.x + dx[i];
                
                if(ny >= 0 && ny < m && nx >= 0 && nx < n ){
                    if (visited[ny][nx]!=true && picture[ny][nx] == picture[current.y][current.x]){
                        visited[ny][nx] = true;
                        size++;
                        q.add(new Node(ny,nx));
                        
                    }
                }
            }
        }
    } 
    
    static class Node{
        
        int y;
        int x;
        
        public Node(int y, int x){
            
            this.y = y;
            this.x = x;
        }
    }
  

}
