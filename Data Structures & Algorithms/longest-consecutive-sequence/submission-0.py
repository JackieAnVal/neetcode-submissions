class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        no_dups = sorted(set(nums))
        lcs = 1
        res = 1
        temp = no_dups[0]
        for i in range(1,len(no_dups)):
            num = no_dups[i]
            if num > temp + 1:
                lcs = 1
            else: 
                lcs += 1
            res = max(res, lcs)
            temp = num
        return res