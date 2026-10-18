class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost)+1)
        cache[1] = 0
        cache[0] = 0
        def dfs(step):
            if step < 0:
                return 0
            
            if cache[step] == -1:
                cache[step] = min(cost[step-1] + dfs(step-1), cost[step-2] + dfs(step-2))
            return cache[step]

        return dfs(len(cost))