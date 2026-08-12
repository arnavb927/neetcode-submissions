class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        high_val = [0] * n
        # low_val = [0] * n
        cur_max = 0
        for i in range(n-1):
            cur_max = max(cur_max, prices[n - i - 1])
            high_val[n - i - 2] = cur_max
        print(high_val)
        diff = [sell - buy for sell, buy in zip(high_val, prices)]
        profit = max(diff)
        if profit < 0:
            return 0
        return profit
