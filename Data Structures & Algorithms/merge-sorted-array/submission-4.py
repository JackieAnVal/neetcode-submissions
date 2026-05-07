class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1[m:] = nums2[:n]
        nums1.sort()
        """
        #MY SOLUTION based on vid MERGE BACKWARDS
        """p1, p2, idx = m-1, n-1, m+n-1

        while p2 >=0:
            if p1>=0 and nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1-=1
            else:
                nums1[idx] = nums2[p2]
                p2-=1
            idx-=1"""
        #Solution 2 MERGE IN ORDER.
        copy = nums1[:m]
        i, p1, p2 = 0, 0, 0
        while i < len(nums1):
            if p2 < n and (p1 >= m or nums2[p2] < copy[p1]):
                nums1[i] = nums2[p2]
                p2 +=1
            else: #termina de copiar copy
                nums1[i] = copy[p1]
                p1 += 1
            i += 1
