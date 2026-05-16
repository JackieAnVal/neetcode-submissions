class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #minimo común múltiplo
        """k = max(piles)
        low = 1
        if h == len(piles):
            return h"""
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                ans = min(ans, k)
                right = k - 1
            else: 
                left = k + 1
        return ans