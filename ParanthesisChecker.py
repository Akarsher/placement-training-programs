from collections import deque
class Solution:
    def isBalanced(self, s):
        # code here
        stack = deque()
        for ch in s :
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            else:
                if stack and ch == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
