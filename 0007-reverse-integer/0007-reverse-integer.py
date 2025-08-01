class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        X = abs(x)
        rev = 0

        while X != 0:

            digit = X % 10
            X = X // 10
            rev = rev * 10 + digit
        
        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev

        
        