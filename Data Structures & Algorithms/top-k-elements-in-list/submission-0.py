class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for i in nums:
            res[i] += 1

        ans = []
        for key, value in res.items():
            ans.append((value, key))

        ans.sort(reverse = True)
        return_val = []
        for i in range(k):
            return_val.append(ans[i][1])
        return return_val