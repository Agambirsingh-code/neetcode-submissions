class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        left= 0
        max_freq = 0
        for i, char in enumerate(s):
            freq[char] +=1
            max_freq = max(max_freq, freq[char])
            if i-left+1 -max_freq > k:
                freq[s[left]] -=1
                left += 1

        return len(s)-left