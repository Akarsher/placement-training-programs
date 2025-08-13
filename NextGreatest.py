class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        res = [-1] * n
        for i in range(n):
            for j in range (i+1,n):
                if arr[i] < arr[j]:
                    res[i] = arr[j]
                    break
        return res
