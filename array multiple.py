'''Churchill was a kindhearted man, and he wanted to give a cakewalk problem to the coders present, to warm them up.

 Given an array of N integers, print the product of the numbers present in the array.

Use appropriate variable types to avoid overflow errors

Input
The first line contains T, the number of test cases.

Each test cases consists of two lines, the first line containing N, the number of elements, and the second line containing N integers.

Output
 For each test case, print the required answer in a single line.'''

t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    p=1
    for j in arr:
        p*=j
    print(p)
