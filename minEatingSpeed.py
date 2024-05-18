class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        def check(k, h, piles):
            count = 0
            for pile in piles:
                count += ceil(pile/k)
            return count <= h

        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid, h, piles):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        