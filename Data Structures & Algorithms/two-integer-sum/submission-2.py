class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        i = 0
        for num in nums:
            diff = target - num
            if diff in d: 
                return [d[diff], i]
            d[num] = i
            i+=1
    """ 
    d = {}
        for i in range(len(nums)): 
            if nums[i] in d: 
                return [d[nums[i]], i]
            else:
                diff = target - nums[i]
                d[diff] = i
    """