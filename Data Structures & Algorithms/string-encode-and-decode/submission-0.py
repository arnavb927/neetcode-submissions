class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            index = s.find('#')
            length = int(s[:index])
            s = s[index+1:]
            res.append(s[:length])
            s = s[length:]
        return res

