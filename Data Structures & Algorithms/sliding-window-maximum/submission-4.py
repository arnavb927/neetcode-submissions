class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxn = max(nums[:k])
        res = [maxn]

        for i in range(k, len(nums)):
            if nums[i] >= maxn:
                maxn = nums[i]


            else:
                if nums[i - k] == maxn:
                    exists = False
                    for j in range(i - k + 1, i):
                        if nums[j] == maxn:
                            exists = True
                            break

                    if not exists:
                        maxn = max(nums[i-k+1:i+1])

        
            res.append(maxn)
        return res