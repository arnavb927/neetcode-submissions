class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(k):
            s1_c = ord(s1[i]) - ord("a")
            s2_c = ord(s2[i]) - ord("a")

            count1[s1_c] += 1
            count2[s2_c] += 1
        
        if count1 == count2:
            return True
        
        for right in range(k, len(s2)):
            s2_c_new = ord(s2[right]) - ord("a")
            count2[s2_c_new] += 1

            s2_c_old = ord(s2[right - k]) - ord("a")
            count2[s2_c_old] -= 1

            if count1 == count2:
                return True
            
        return False
            

            

