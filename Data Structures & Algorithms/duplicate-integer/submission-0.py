class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = set(nums)
        if len(t) == len(nums):
            return False
        else:
            return True