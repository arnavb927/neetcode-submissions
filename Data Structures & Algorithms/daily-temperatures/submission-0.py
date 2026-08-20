class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temperatures = list(enumerate(temperatures))

        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)-1, -1, -1):
            if not stack:
                stack.append(temperatures[i])
                res[i] = 0
                continue

            if stack[-1][1] > temperatures[i][1]:
                stack.append(temperatures[i])
                res[i] = 1
                continue



            while stack and stack[-1][1] <= temperatures[i][1]:
                stack.pop()



            if stack and stack[-1][1] > temperatures[i][1]:
                res[i] = stack[-1][0] - temperatures[i][0]
                stack.append(temperatures[i])
                continue
            else:
                stack.append(temperatures[i])
                res[i] = 0
                continue

        return res

