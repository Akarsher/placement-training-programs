from collections import deque
class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        stack = deque()
        res = [-1] * n
        for i in range(n-1,-1,-1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = arr[stack[-1]]
            stack.append(i)
        return res
        
