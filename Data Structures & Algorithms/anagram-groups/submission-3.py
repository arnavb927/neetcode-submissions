class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in range(len(strs)):
            res[''.join(sorted(strs[i]))].append(strs[i])

        return list(res.values())
