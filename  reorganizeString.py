class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        heap = []
        for char, count in count.items(): # min heap is default so doing this to get maxheap
            priority = -count  
            pair = (priority, char)
            heap.append(pair)
        heapq.heapify(heap)

        prev = None
        res = ""
        while heap:
            count, char = heapq.heappop(heap) # most frequent value w/o prev
            res += char
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count != 0:
                prev = (count, char)
        
        if prev: # heap is empty and we still have prev value and it is the repeating char
            return ""
        return res
