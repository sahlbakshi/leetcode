class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dictionary = {}
        for char in text:
            dictionary[char] = dictionary.get(char, 0) + 1
        balloon = Counter('balloon')
        # could also do for text
    
        count = len(text)
        for c in balloon:
            if c not in dictionary:
                return 0
            count = min(count, dictionary[c] // balloon[c])
            # double division iport because we want integer
            # make sure to check not condition
        return count
        