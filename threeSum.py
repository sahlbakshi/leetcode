class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort() # sorting to avoid duplicates
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    second = nums[left]
                    third = nums[right]
                    res.append([nums[i], second, third])
                    while left < right and nums[left] == second:
                        left += 1
                    while left < right and nums[right] == third:
                        right -= 1
        return res
