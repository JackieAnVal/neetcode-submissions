class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """res = Counter(nums)
        l = sorted(res.keys(), key=res.get, reverse=True)
        return l[:k]"""
        # 1. Contar frecuencias: O(N)
        counts = Counter(nums)

        # 2. Hacer buckets
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in counts.items():
            bucket[freq].append(num)
        
        res = []
        # Get k most frequent nums from bucket(trick: reverse)
        for b in reversed(bucket): 
            for n in b:
                res.append(n)
                if len(res) == k: # Tienes que detenerte cuando llegues a k
                    return res