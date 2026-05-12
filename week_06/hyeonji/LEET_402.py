class Solution:
    def removeKdigits(self, num, k):

        stack = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack)

        result = result.lstrip('0')

        return result if result else "0"