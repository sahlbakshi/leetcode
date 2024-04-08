class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        i = len(nums) - 2
        goal = i + 1

        while i >= 0:
            if i + nums[i] >= goal:
                goal = i
            i -= 1

        if goal == 0:
            return True
        return False
