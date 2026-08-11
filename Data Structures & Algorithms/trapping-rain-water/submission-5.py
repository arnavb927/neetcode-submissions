class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        arrlr = []
        arrrl = []
        max_h = 0
        for i in range(0, len(height)-1):
            max_h = max(max_h, height[i])
            arrlr.append(max_h)
        max_h = 0
        for i in range(len(height)-1, 0, -1):
            max_h = max(max_h, height[i])
            arrrl.append(max_h)
        arrrl = arrrl[::-1]


        for i in range(len(height) - 2):
            cur_water = min(arrlr[i], arrrl[i])
            cur_water -= height[i+1]
            if cur_water < 0:
                cur_water = 0
            water += cur_water
        return water

            
        