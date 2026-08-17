class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        subs = list(s2[l : r])
        s1_sorted = sorted(s1)

        if sorted(subs) == s1_sorted:
            return True
    
        while r < len(s2):
            if sorted(subs) == s1_sorted:
                return True
            subs.pop(0)
            subs.append(s2[r])
            r += 1

            if sorted(subs) == s1_sorted:
                return True

        return False

            

            

