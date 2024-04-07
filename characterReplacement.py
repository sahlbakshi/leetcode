class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        charmap = {}
        longest = 0
        topF = 0

        left = 0
        right = 0

        while (right < len(s)):
            charmap[s[right]] = 1 + charmap.get(s[right], 0)
            topF = max(charmap.values())

            # window is right - left + 1
            if (right - left + 1) - topF > k:
                charmap[s[left]] -= 1
                left += 1
                topF = max(charmap.values())

            longest = max(longest, right - left + 1)
            right += 1
        
        return longest
