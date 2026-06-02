class Solution {
    public String solution(String number, int k) {
        StringBuilder stack = new StringBuilder();

        for (int i = 0; i < number.length(); i++) {
            char current = number.charAt(i);

            while (k > 0 && stack.length() > 0
                    && stack.charAt(stack.length() - 1) < current) {
                stack.deleteCharAt(stack.length() - 1);
                k--;
            }

            stack.append(current);
        }

        if (k > 0) {
            stack.delete(stack.length() - k, stack.length());
        }

        return stack.toString();
    }
}