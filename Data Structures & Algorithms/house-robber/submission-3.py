class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(start):
            if cache[start] == -1:
                if start+3 < len(nums):
                    cache[start] = max(nums[start] + dfs(start+2), nums[start] + dfs(start+3))
                elif start+2 < len(nums):
                    cache[start] = nums[start] + dfs(start+2)
                else:
                    cache[start] = nums[start]
                
            
            return cache[start]
        if len(nums) <= 1:
            return nums[0]
        else:
            return max(dfs(0), dfs(1))
                