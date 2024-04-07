class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open if open < n
        # only add close if close < open
        # valid iff open == lcoses == n otherwise we stop

        output = []

        def backtrack(openN, closeN, s):
            if len(s) == 2*n:
                output.append(s)
                return
            
            if openN < n:
                backtrack(openN + 1, closeN, s + '(')
            
            if closeN < openN:
                backtrack(openN, closeN + 1, s + ')')
        
        backtrack(0, 0, "")
        return output
