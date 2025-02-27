''' Given a sorted array 
a
r
r
arr, remove the duplicates from 
a
r
r
arr such that each element appears only once and display the new array.

Input:
The first line contains 
T
T, the number of test cases. Then the 
T
T test cases follow.
Each test case contains 
2
2 lines of input:
The first line contains 
n
n, the size of array 
a
r
r
arr.
The second line contains 
n
n space separated elements of array 
a
r
r
arr.
Output:
For each test case, output in a single line, the new array. The elements of the array should be separated by space. Your output format should match with that given in the sample output.'''

t=int(input())
while t!=0:
   n=int(input())
   a=list(set(int(i) for i in input().split()))
   for i in a:
      print(i,end=" ")
   t=t-1
