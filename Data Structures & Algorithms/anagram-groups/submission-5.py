class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dick = {}

        for i in strs:
            if str(sorted(i)) not in dick:
                dick[str(sorted(i))] = [i]
            else:
                dick[str(sorted(i))].append(i)
        
        return list(dick.values())