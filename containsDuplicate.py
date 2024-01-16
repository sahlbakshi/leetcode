class Solution(object):
    def containsDuplicate(self, nums):
        
        """
        :type nums: List[int]
        :rtype: bool
        """

        dictionary = {}
        for num in nums:
            if num in dictionary:
                return True
            else:
                dictionary[num] = 1
        return False
