class Solution(object):
    def search(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        pivot = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                pivot = i
                break
        
        l = 0
        r = 0
        if target >= nums[0] and target <= nums[pivot]:
            l = 0
            r = pivot
        else:
            l = pivot+1 
            r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
        
        return -1
