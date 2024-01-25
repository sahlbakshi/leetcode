class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            area = (r - l) * min(height[l], height[r]) # min because it has to cover
            maxArea = max(area, maxArea)
            if height[l] >= height[r]: # doesnt matter which one we go to when ==
                r -= 1
            elif height[l] < height[r]:
                l += 1

        return maxArea
