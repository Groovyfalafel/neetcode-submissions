class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 1
        zero_count = nums.count(0)

        for i in nums:
            if i != 0:
                total *= i
        if zero_count > 1:
            for i in nums:
                output.append(0)

        elif zero_count == 1:
            for i in nums:
                if i == 0:
                    output.append(total)
                else:
                    output.append(0)
        else:
            for i in nums:
                output.append(total // i)


        return output


        