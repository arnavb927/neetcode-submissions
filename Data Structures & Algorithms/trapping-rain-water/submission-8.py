class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        arrlr = []
        arrrl = []
        max_lr = 0
        n = len(height)
        max_rl = 0
        for i in range(0, len(height)-1):
            max_lr = max(max_lr, height[i])
            arrlr.append(max_lr)

            max_rl = max(max_rl, height[n - 1 - i])
            arrrl.append(max_rl)

        arrrl = arrrl[::-1]
        
        min_h = [min(x, y) for x,y in zip(arrrl, arrlr)]

        final = [0 if x-y<0 else x-y for x,y in zip(min_h, height[1:-1])]
        return sum(final)
        
        # for i in range(len(height) - 2):
        #     cur_water = min(arrlr[i], arrrl[i])
        #     cur_water -= height[i+1]
        #     if cur_water < 0:
        #         cur_water = 0
        #     water += cur_water
        # return water

            
        