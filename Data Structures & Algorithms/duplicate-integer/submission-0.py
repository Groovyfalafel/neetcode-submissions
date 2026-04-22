class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for idx in range(len(sorted_nums) - 1):
            if sorted_nums[idx] == sorted_nums[idx + 1]:
                return True
        return False
