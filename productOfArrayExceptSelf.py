class Solution(object):
    def productExceptSelf(self, nums):
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # we keep a left array representing the product of elements on left side of index i
        # we keep a right array representing the product of elements on right side of index i
        # to get product value at i we will just multiply left and right side excluding i

        size = len(nums)
        left = [1] * size
        right = [1] * size

        left[0] = nums[0]
        for i in range(1, size): # iterating from 1 to end
            left[i] = left[i-1] * nums[i]
        
        right[size-1] = nums[size-1]
        for i in range(size-2, -1, -1): # iterating from size-2 to 0
            right[i] = right[i+1] * nums[i]

        ans = [1] * size
        for i in range(size):
            if i-1 < 0:
                ans[i] = right[i+1]
            elif i+1 == size:
                ans[i] = left[i-1]
            else:
                ans[i] = left[i-1] * right[i+1]
        
        return ans
