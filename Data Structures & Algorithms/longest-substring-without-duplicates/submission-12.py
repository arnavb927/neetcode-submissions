class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_letters = {}
        length = 0
        max_length = 0
        prev_idx = 0
        for i in range(len(s)):
            #duplicate found
            try:
                #deactivated
                if cur_letters[s[i]] < 0:
                    cur_letters[s[i]] = i
                    length += 1
                    max_length = max(max_length, length)
                    continue
                #activated
                else:
                    waste = cur_letters[s[i]] + 1
                    length -= cur_letters[s[i]]
                    length += prev_idx
                    for j in range(prev_idx, waste):
                        cur_letters[s[j]] = -1
                    prev_idx = waste
                    cur_letters[s[i]] = i
                    # print(cur_letters)

            except KeyError:
                #new letter being added
                cur_letters[s[i]] = i
                length += 1
            max_length = max(max_length, length)

        return max_length

