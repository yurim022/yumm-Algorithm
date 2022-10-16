package programmers;

import java.util.*;

public class Solution {
    public int solution(int n) {
        //top-down 방식의 처리, n이 짝수이면 /2로 순간이동 하고 홀수일 경우 점프
        int usedCount = 0;
        
        while ( n > 0) {
            if (n % 2 == 0){ //순간이동
                n /= 2;
                continue;
            }
            
            //점프
            n -= 1;
            usedCount += 1;
        }
        
        return usedCount;
    }
}
