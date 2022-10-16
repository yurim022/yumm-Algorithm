package programmers;

import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        Stack<Integer> remove = new Stack<>();
        int table_size = n;
        
        for(int i = 0; i < cmd.length; ++i){
            char c = cmd[i].charAt(0);
        

            if(c == 'U'){
                k -= Integer.valueOf(cmd[i].substring(2));
            }else if(c == 'D'){
                k += Integer.valueOf(cmd[i].substring(2));
            }else if(c == 'C'){
                remove.push(k);
                table_size -= 1;
                if(k == table_size) k -= 1;
            }else{
                int r = remove.pop();
                table_size += 1;
                if(k >= r) k+= 1;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i< table_size; ++i){
            sb.append('O');
        }
        
        while( !remove.isEmpty()){
            sb.insert(remove.pop().intValue(),'X');
        }
        return sb.toString();
    }
}


----
    
    
    
    
    
    //LinkedList 풀이
    
    
    
    
    import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        Node cur = initList(n);
        Stack<Node> stack = new Stack<>();
        for (int i = 0; i < k; i++) {
            cur = cur.next;
        }

        for (String s : cmd) {
            char command = s.charAt(0);
            int distance;
            switch (command) {
                case 'U':
                    distance = getDistance(s);
                    for (int i = 0; i < distance; i++) {
                        cur = cur.prev;
                    }
                    break;
                case 'D':
                    distance = getDistance(s);
                    for (int i = 0; i < distance; i++) {
                        cur = cur.next;
                    }
                    break;
                case 'C':
                    stack.add(cur);
                    cur.remove();
                    cur = cur.hasNext() ? cur.next : cur.prev;
                    break;
                case 'Z':
                    stack.pop().restore();
                    break;
            }
        }

        StringBuilder answer = new StringBuilder("O".repeat(n));
        while (!stack.isEmpty()) {
            answer.setCharAt(stack.pop().idx, 'X');
        }
        return answer.toString();
    }

    private int getDistance(String s) {
        return Integer.parseInt(s.substring(2));
    }

    private static class Node {
        int idx;
        Node prev, next;

        public Node(int idx) {
            this.idx = idx;
        }

        boolean hasNext() {
            return next.idx != -1;
        }

        public void restore() {
            prev.next = this;
            next.prev = this;
        }

        public void remove() {
            prev.next = next;
            next.prev = prev;
        }
    }

    private Node initList(int n) {
        Node start = new Node(-1);
        Node prev = start;
        Node cur = null;
        for (int i = 0; i < n; i++) {
            cur = new Node(i);
            prev.next = cur;
            cur.prev = prev;
            prev = cur;
        }
        cur.next = new Node(-1); //end노드 설정
        return start.next; //첫번째 노드 반환
    }
}

