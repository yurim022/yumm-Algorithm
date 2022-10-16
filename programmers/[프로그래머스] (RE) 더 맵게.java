package programmers;

import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        //일반적으로 python이 빠르나, 효율성 테스트에서는 java가 이김
        int cnt = 0;
        PriorityQueue<Integer> pq = new PriorityQueue();
        
        //우선순위 큐에 파일 넣기
        for (int s:scoville){
            pq.offer(s);
        }
        //K보다 커질때까지 연산
        while(pq.peek()<K){
            if(pq.size()==1){return -1;}
            pq.offer(pq.poll()+pq.poll()*2);
            cnt ++;
        }
        return cnt;
    }
}
