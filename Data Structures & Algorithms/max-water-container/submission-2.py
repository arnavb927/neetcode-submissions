class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = sorted([(val, idx) for idx, val in enumerate(heights)], reverse=True)
        n = len(heights)
        max_a = 0
        l = 0
        r = n-1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_a = max(max_a, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_a

