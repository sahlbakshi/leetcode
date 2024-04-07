class Solution(object):
    def groupAnagrams(self, strs):
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # we go trough the strings
        # sort it and add to dictionary if not already there
        # otherwise append it to the already added one

        hashmap = {}
        for elem in strs:
            temp = ''.join(sorted(elem)) # sorted sorts but makes array so we have to join them
            if temp in hashmap:
                hashmap.get(temp).append(elem) # hashmap[temp].append(elem) also works
            else:
                hashmap[temp] = [elem]

        ans = []
        for k, v in hashmap.items(): # need to use .items to iterate over
            ans.append(v)

        return ans
    