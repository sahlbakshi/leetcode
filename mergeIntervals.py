class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        prev = 0
        for start, end in intervals[1:]: # starts from second element as first is already in array
            if start <= res[prev][1]:
                # intervals[prev][0] stays as it is
                res[prev][1] = max(end, res[prev][1])
            else:
                res.append([start, end])
                prev += 1
        return res
