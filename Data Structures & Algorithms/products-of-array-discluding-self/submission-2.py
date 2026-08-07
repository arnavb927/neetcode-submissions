class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = [1] * length
        suf = [1] * length

        for i in range(-2, -length-1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        for i in range(1, length):
            pre[i] = pre[i-1] * nums[i-1]

        
        for i in range(length):
            pre[i] = pre[i] * suf[i]
            
        return pre

