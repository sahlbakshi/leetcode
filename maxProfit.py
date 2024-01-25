class Solution(object):
    def maxProfit(self, prices):

        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)
        return profit

        # we only change left pointer as in minprice if we find new minimum
        # otherwise we just keep calculating the profit as we go on
        # have to check min price and calulate profits as we go along
        # if we find new minimum doesnt mean that max profit will be with that value
