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
        temp = x
        length = 0
        while temp > 0:
            length += 1
            temp //= 10
        
        y = 10 ** (length - 1)

        while x > 0:
           output += (x % 10) * y
           y //= 10
           x //= 10

        output *= sign

        if output < MIN or output > MAX:
            return 0

        return output