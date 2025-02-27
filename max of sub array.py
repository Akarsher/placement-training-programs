''' There are N hotels along the beautiful Adriatic coast. Each hotel has its value in Euros.

Sroljo has won M Euros on the lottery. Now he wants to buy a sequence of consecutive hotels, such that the sum of the values of these consecutive hotels is as great as possible - but not greater than M.

You are to calculate this greatest possible total value.

Input
In the first line of the input there are integers N and M (1 ≤ N ≤ 300 000, 1 ≤ M < 231).

In the next line there are N natural numbers less than 106, representing the hotel values in the order they lie along the coast.

Output
Print the required number (it will be greater than 0 in all of the test data).'''
n,m = map(int,input().split())
arr=list(map(int,input().split()))
smax=0
s=0
st=0
for i in range(n):
    s+=arr[i]
    while s>m:
        s-=arr[st]
        st+=1
    smax=max(smax,s)
print(smax)
