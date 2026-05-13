class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums) #6
        left, right = 0, l - 1 # 0, 5
        while left <= right: 
            middle = left + (right - left) // 2 # 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1