class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return res
