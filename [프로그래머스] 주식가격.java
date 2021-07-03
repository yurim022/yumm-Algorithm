import java.util.*;


class Solution {
    public int[] solution(int[] prices) {
        
        //주식가격이 떨어지지 않았다 에서 -> stack 을 생각하는 키워드!
        
        int[] ans = new int[prices.length];
        Stack<Integer> stack = new Stack();
        
        for (int i = 0; i < prices.length; i++){
            while (!stack.isEmpty() && prices[i] < prices[stack.peek()]) {
                ans[stack.peek()] = i - stack.peek(); //주식가격이 떨어짐
                stack.pop(); //답을 구했기 때문에 stack에서 제거
            }
            stack.push(i);
        }
        
        while(!stack.isEmpty()){//값을 구하지 못한 index == 끝까지 가격이 떨어지지 않은 주식
            ans[stack.peek()] = (prices.length-1) - stack.peek();
            stack.pop();
        }
        
        return ans;
    }

}
