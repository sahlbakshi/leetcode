class Solution(object):
    def longestConsecutive(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """

        # we count all the lengths as we encounter the subsequences and output the largest one
        # using a set makes this very easy to do
        
        numset = set(nums)
        length = 0
        longest = 0

        for num in nums:
            if num-1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                longest = max(length, longest)
        return longest
        