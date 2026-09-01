class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)

        times = [-1] * len(cars)
        for i in range(len(cars)):
            times[i] = (target - cars[i][0])/cars[i][1]


        stack = []
        num_fleet = 0
        for i in range(len(times)):
            if len(stack) == 0:
                num_fleet += 1
                stack.append(times[i])
                continue
            
            if stack[0] >= times[i]:
                stack.append(times[i])
            else:
                num_fleet += 1
                stack = [times[i]]
        
        return num_fleet