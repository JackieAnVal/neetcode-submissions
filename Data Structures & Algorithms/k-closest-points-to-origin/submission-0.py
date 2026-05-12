class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidian = []
        for x, y in points:
            dist = (x ** 2) + (y**2)
            euclidian.append([dist, x, y])
        
        heapq.heapify(euclidian)

        res = []
        while k > 0:
            eu, x, y = heapq.heappop(euclidian)
            res.append([x, y])
            k-=1
        return res