class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        result = 0
        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            #if x < y:
            diff = abs(x-y)
            heapq.heappush_max(stones, diff)
        
        if stones:
            result = stones[0]
        return result