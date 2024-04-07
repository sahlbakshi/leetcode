class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        count = 0
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prevEnd: # are overlapping
                prevEnd = min(end, prevEnd)
                count += 1
            else:
                prevEnd = end
        return count
