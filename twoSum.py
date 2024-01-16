class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        size = len(nums) # getting size of nums
        hashmap = {} # value / difference : index
        for i in range(size):
            diff = target - nums[i]
            if diff in hashmap: # seeing value
                return [i, hashmap[diff]]
            else:
                hashmap[nums[i]] = i
