class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', "]":'[', ")":"("}

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        return not stack
 