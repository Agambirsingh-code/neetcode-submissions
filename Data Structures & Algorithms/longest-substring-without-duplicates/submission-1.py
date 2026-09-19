class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_count = 0

        for i in range(len(s)):
            if s[i] in seen:
                left = max(seen[s[i]]+1,left)
            seen[s[i]] = i
            max_count = max(max_count, i-left+1)
        return max_count