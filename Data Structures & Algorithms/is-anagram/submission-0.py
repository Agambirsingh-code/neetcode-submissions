class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key1 = "".join(sorted(s))
        key2 = "".join(sorted(t))
        if key1 == key2:
            return True

        return False