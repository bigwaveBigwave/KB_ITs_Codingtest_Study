class Solution {
    public int[] solution(String s) {
        char[] cArr = s.toCharArray();
        int iterCnt = 0;
        int removeCnt = 0; 
        
        while (cArr.length > 1) {
            iterCnt++;
            int binaryCnt = 0;
            
            for (int i = 0; i < cArr.length; i++) {
                if (cArr[i] == '1') binaryCnt++;
                else removeCnt++;
            }
            
            String binaryExp = Integer.toBinaryString(binaryCnt);
            cArr = binaryExp.toCharArray();
        }
        
        return new int[] {iterCnt, removeCnt};
    }
}
