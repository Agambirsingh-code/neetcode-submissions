class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        if len(nums) == 2 and (nums[0]+nums[1]) == target:
            return [0,1]
        for i, num in enumerate(nums):
            complement = target- num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i