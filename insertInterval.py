class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        # intervals already sorted so dont have to do that
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # happens if new interval comes before
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # happens if new interval comes after
                res.append(intervals[i])
            else:  # happens if new interval comes in middle
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res
