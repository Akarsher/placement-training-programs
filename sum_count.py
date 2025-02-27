''' Leonard was always sickened by how Sheldon considered himself better than him. To decide once and for all who is better among them they decided to ask each other a puzzle. Sheldon pointed out that according to Roommate Agreement Sheldon will ask first. Leonard seeing an opportunity decided that the winner will get to rewrite the Roommate Agreement.

Sheldon thought for a moment then agreed to the terms thinking that Leonard will never be able to answer right. For Leonard, Sheldon thought of a puzzle which is as follows. He gave Leonard n numbers, which can be both positive and negative. Leonard had to find the number of continuous sequence of numbers such that their sum is zero.

For example if the sequence is: 5, 2, -2, 5, -5, 9, there are 3 such sequences:

2, -2
5, -5
2, -2, 5, -5
Since this is a golden opportunity for Leonard to rewrite the Roommate Agreement and get rid of Sheldon's ridiculous clauses, he can't afford to lose. So he turns to you for help. Don't let him down.

Input
First line contains T - number of test cases

Second line contains n - the number of elements in a particular test case.

Next line contain n elements, ai (1 ≤ i ≤ n) separated by spaces.

Output
The number of such sequences whose sum if zero.'''

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    Sum = {0: 1}
    csum = 0
    count = 0
    for j in arr:
        csum += j
        if csum in Sum:
            count += Sum[csum]
        
        if csum in Sum:
            Sum[csum] += 1
        else:
            Sum[csum] = 1 
    print(count)
