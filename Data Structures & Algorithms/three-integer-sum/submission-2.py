class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(list(nums))
        res = []
        for i in range(len(sorted_nums)-2):
            if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
                continue
            target = 0 - sorted_nums[i]
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == target:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])

                    while l < r and sorted_nums[l + 1] == sorted_nums[l]:
                        l += 1
                    while l < r and sorted_nums[r-1]  == sorted_nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
        return res
            


            