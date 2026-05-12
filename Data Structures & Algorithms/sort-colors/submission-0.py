class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for num in nums:
            buckets[num] +=1
            #  0, 1, 2 
            # [1, 2, 1]
        idx = 0
        for i in range(len(buckets)):
            for j in range(buckets[i]):
                nums[idx]=i
                idx +=1
        return nums