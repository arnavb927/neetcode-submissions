class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        
        res = "".join(parts)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            if not s:
                break
            index = s.find('#', i)
            length = int(s[i:index])
            i = index + 1
            res.append(s[i:i+length])
            i += length
        return res

