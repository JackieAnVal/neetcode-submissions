class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        i = 0
        for num in nums:
            diff = target - num
            if num in d: 
                return [d[num], i]
            else:
                d[diff] = i
            i+=1