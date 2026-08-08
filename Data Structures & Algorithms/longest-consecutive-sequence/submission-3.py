class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        max_length = 0
        cur_length = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                cur_length += 1
            else:
                max_length = max(cur_length, max_length)
                cur_length = 1
        if not nums:
            return 0
        max_length = max(cur_length, max_length)
        return max_length