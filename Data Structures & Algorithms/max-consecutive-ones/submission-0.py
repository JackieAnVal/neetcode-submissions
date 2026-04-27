class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        counter = 0
        for num in nums:
            if num ==1: 
                counter+=1
                max_ones = max(max_ones, counter)
            else:
                counter = 0
        return max_ones