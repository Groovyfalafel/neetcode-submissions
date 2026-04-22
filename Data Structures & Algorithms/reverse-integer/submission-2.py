class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 -1


        if x == 0:
            return 0

        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        output = 0
        

        while x > 0:
           digit = x % 10
           output = output * 10 + digit
           x //= 10
           

        output *= sign

        if output < MIN or output > MAX:
            return 0

        return output