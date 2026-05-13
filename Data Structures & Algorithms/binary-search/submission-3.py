class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right = 0, l - 1
        while left <= right: 
            #(r -l) sólo calcula la diferencia pero no indica la posición de middle aún, 
            #por eso se le suma l y luego dividimos entre dos para obtener el índice de enmedio
            middle = left + (right - left) // 2 # middle = left + right // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1