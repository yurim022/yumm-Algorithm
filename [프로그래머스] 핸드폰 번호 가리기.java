class Solution {
    public String solution(String phone_number) {
        StringBuilder sb = new StringBuilder("*".repeat(phone_number.length()-4));
        sb.append(phone_number.substring(phone_number.length()-4));
        return sb.toString();
    }
}

--------
  
  //밑에꺼가 정규식이긴 한데 위에 풀이가 10배정도 빠름..!!
  
  class Solution {
    public String solution(String phone_number) {
        return phone_number.replaceAll(".(?=.{4})","*");
    }
}
