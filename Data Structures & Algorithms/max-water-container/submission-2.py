class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            hl , hr = heights[l], heights[r]
            temp_area = (min(hl, hr)) * (r - l)
            max_area = max(temp_area, max_area)
            if hl <= hr:
                l += 1
            else:
                r -= 1
        return max_area