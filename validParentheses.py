class Solution(object):
    def isValid(self, s):

        """
        :type s: str
        :rtype: bool
        """

        Map = { "}" : "{", "]" : "[", ")": "(" }
        stack = []
        for char in s:
            if char not in Map:
                stack.append(char)
            else:
                if not stack: # empty because starts with closing
                    return False
                elem = stack.pop()
                if elem != Map[char]:
                    return False # closes incorrectly
        if stack: # characters remaining
            return False 
        return True
