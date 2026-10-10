class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in mapping:
                open_bracket = stack.pop() if stack else '#'
                if mapping[i] != open_bracket:
                    return False
            else:
                stack.append(i)
        return not stack
