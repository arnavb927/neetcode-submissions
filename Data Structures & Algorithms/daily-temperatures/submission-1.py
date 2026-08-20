class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(set(temperatures)) == 1:
            return [0] * len(temperatures)
        
        res = []

        n = len(temperatures)

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res
