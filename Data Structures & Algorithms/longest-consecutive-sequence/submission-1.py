class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for i in numSet:
            if i - 1 not in numSet:
                counter = 1
                while i + counter in numSet:
                    counter += 1
                
                if counter > longest:
                    longest = counter
                
        return longest