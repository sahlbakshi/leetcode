class Solution(object):
    def topKFrequent(self, nums, k):
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # what is the maximum size of array that can occur?
        # we know that it is the size of the array - need this becasue we want to make an array 
        # where each count is the index that holds the value that it counts

        size = len(nums)
        arr = []
        for i in range(size):
            arr.append([])

        # nums.sort() - when we use lists we have to srot becasue we compare but when we use dictionaries we dont have to
        
        dictionary = {}
        for i in range(size):
            if (nums[i] in dictionary):
                dictionary[nums[i]] = dictionary.get(nums[i]) + 1
            else:
                dictionary[nums[i]] = 1
        
        for j, v in dictionary.items(): # do not use k instead of j as it messes with the k value for most frequent elements
            arr[v-1].append(j) # v-1 because goes outside range if for exmaple freq = 5 and list size = 5
        
        ans = []
        for i in reversed(arr): # we start from the end with largest frequency value
            for num in i:
                if k > 0:
                    ans.append(num)
                    k -= 1
                else:
                    break
        
        return ans
    


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        arr = [[] for i in range(len(nums))]
        hmap = Counter(nums)

        for i, j in hmap.items():
            arr[j-1].append(i)
        
        res = []
        for i in reversed(arr):
            for num in i:
                if k > 0:
                    res.append(num)
                    k -=1
        return res
        