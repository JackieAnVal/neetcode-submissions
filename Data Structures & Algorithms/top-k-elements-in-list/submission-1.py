class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """res = Counter(nums)
        l = sorted(res.keys(), key=res.get, reverse=True)
        return l[:k]"""
        # 1. Contar frecuencias: O(N)
        counts = Counter(nums)
        
        # 2. Crear cubetas: El índice es la frecuencia, el valor es una lista de números
        # Tamaño len(nums) + 1 porque un número puede aparecer N veces
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        # 3. Recolectar los k más frecuentes: O(N)
        res = []
        # Recorremos desde la frecuencia más alta (final del array) hacia abajo
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res