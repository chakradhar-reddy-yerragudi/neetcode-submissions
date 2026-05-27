class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'{':'}','[':']','(':')'}
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if not stack or d[stack[-1]]!=c:
                    return False
                stack.pop()
        return not stack 