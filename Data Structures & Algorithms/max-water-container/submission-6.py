class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_a = 0
        l = 0
        r = n-1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_a = max(max_a, area)
            if heights[l] > heights[r]:
                curr = r
                for i in range(r-1, -1, -1):
                    if heights[curr] < heights[i]:
                        r = i
                        break
                if curr == r:
                    break

            else:
                curr = l
                for i in range(l+1, r):
                    if heights[curr] < heights[i]:
                        l = i
                        break
                if curr == l:
                    break

        return max_a

