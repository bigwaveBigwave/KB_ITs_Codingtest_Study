class Solution {
    public String solution(String number, int k) {
        String answer = "";
//         int len = number.length();
//         int numLen = len - k;
//         int max = 0;
//         while (k > 0) {
//             int l = number.length();
//             for (int i = 0 ; i < l; i++) {
//                 String temp = number.substring(0,i) + number.substring(i+1);     이런식으로 하면 시간이 너무 오래걸린다네???
//             }
//             int tempNum = Integer.parseInt(temp);
//             if (max < tempNum) {
//                 max = tempNum;
//             }

//             k-=1;
//         }
//         answer = String.valuOf(max);

        StringBuilder sb = new StringBuilder();
        int len = number.length();

        for (int i = 0 ; i < len ; i++) {
            char current = number.charAt(i);

            while(sb.length() > 0 &&  k > 0 && sb.charAt(sb.length() - 1) < current) {
                sb.deleteCharAt(sb.length()-1);
                k--;
            }
            sb.append(current);
        }
        answer = sb.substring(0, sb.length()-k);
        return answer;
    }
}