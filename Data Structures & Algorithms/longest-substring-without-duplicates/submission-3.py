class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bum = {} 
        max_length = 0
        current_length = 0
        start_of_new = 0

        for i in range(len(s)): 
            if s[i] not in bum or bum[s[i]] < start_of_new:
                bum[s[i]] = i
                current_length += 1
            else: 
                max_length = max(current_length, max_length)
                current_length = i - bum[s[i]] 
                start_of_new = bum[s[i]] + 1
                bum[s[i]] = i

        max_length = max(current_length, max_length)

        return max_length