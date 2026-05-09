class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        l = sorted(res.keys(), key=res.get, reverse=True)
        return l[:k]