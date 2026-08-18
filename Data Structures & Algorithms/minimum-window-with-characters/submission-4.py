class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return s

        l = -1
        for i in range(len(s)):
            if s[i] in t:
                l = i
                break

        all_lets = {}
        for i in range(len(t)):
            all_lets[t[i]] = 1 + all_lets.get(t[i],0)
        print(all_lets)

        if l == -1:
            return ""

        all_lets[s[l]] -= 1
        words = []
        if s[l] == t:
            return t
        for r in range(l+1, len(s)):
            if s[r] in t:
                if all_lets[s[r]] <= 0 and s[r] == s[l]:
                    l += 1
                    while s[l] not in t:
                        l += 1
                    while s[l] in s[l+1:r+1] and all_lets[s[l]] < 0:
                        all_lets[s[l]] += 1
                        l += 1
                        while s[l] not in t:
                            l += 1

                else:
                    all_lets[s[r]] -= 1
                
            # print(all_lets)
            if all(v <= 0 for v in all_lets.values()):
                words.append(s[l:r+1])
            
        # print(words)
        if len(words) == 0:
            return ""
        return min(words, key=len)

            

            