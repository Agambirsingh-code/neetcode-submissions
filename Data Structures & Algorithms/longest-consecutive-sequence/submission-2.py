class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        max_count = 1
        nums.sort()

        if len(nums) == 0:
            return 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i]+1 == nums[i+1]:
                count += 1
            else: 
                count = 1
            if max_count < count:
                max_count = count
        return max_count