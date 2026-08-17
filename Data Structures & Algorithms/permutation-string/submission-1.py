class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        
        for i in range(len(s2) - len(s1) + 1):
            subs = s2[l + i : r + i]
            if sorted(subs) == sorted(s1):
                return True
        return False

            

            

