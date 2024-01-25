class Solution(object):
    def lengthOfLongestSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        
        longest = 0
        string = ""
        chars = set()
        for i in range(len(s)):
            j = i
            while j < len(s):
                if s[j] not in chars:
                    chars.add(s[j])
                    string += s[j]
                    j += 1
                else:
                    longest = max(longest, len(string))
                    string = ""
                    chars.clear()
                    break
        if longest == 0: # for when we never come to else statement - all unique chars
            return len(string)
        return longest
