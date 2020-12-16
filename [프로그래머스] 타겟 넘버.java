class Solution {
    public int solution(int[] numbers, int target) {
    
        return DFS(numbers,0,0, target);
    
    }
    
    public int DFS(int[] numbers,int idx,int sum, int target){
        if(idx == numbers.length && sum == target ) return 1;
        else if(idx == numbers.length) return 0;
        else return DFS(numbers,idx+1,sum+numbers[idx],target)+ DFS(numbers,idx+1,sum-numbers[idx],target);
    }
}
