class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if len(stack) == 0:
                    return False
                elif pair[ch] != stack[-1]:
                    return False

                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False