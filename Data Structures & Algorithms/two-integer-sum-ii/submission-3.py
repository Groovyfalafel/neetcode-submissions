class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        output = []
        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left +=1
            else:
                output.append(left + 1)
                output.append(right + 1)
                return output