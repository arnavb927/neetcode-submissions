class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = []
        for i in s:
            if not i.isalnum():
                continue
            else:
                sentence.append(i.lower())
        
        print(sentence)
        length = len(sentence)
        i = 0
        while i < length - i:
            if sentence[i] != sentence[length-i - 1]:
                return False
            i += 1
        return True