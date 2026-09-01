class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            cur_idx = (l+r) // 2
            if nums[cur_idx] == target:
                return cur_idx
            elif nums[cur_idx] < target:
                l = cur_idx + 1
            else:
                r = cur_idx - 1


        return -1 