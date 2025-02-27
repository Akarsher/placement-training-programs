'''Vishal Wants to buy 2 gifts for his best friend whose name is Annabelle(her age is 20), So they both went for shopping in a store. But Annabelle gave, Vishal a condition that she will accept this gifts only when the total price of the gifts is the same as her age times 100.

The store contains, a list of items whose prices are also displayed, Now Vishal is asking for your help to buy gifts, as he wants to impress Annabelle this time.

Note: Vishal cannot buy the same item more than once.

Input:
The first line of the input contains a single integer 
T
T. 
T
T denoting the number of test cases. The description of 
T
T test cases is as follows.
The next line of the input contains a single integer 
N
N. 
N
N denotes the total number of items in store.
The next line of the input contains 
N
N space-separated integers 
A
1
,
A
2
,
A
3...
A
n
A1,A2,A3...An where 
i
t
h
ith number denotes the price of 
i
t
h
ith element.
Output:
For each test-case print “Accepted”(without quotes) if the gifts are accepted by Annabelle, else print “Rejected”(without quotes)'''

t=int(input())
while t>0:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    i=0
    j=n-1
    flag=0
    while(i<j):
        if arr[i]+arr[j]==2000:
            flag=1
            break
        elif arr[i]+arr[j]<2000:
            i=i+1
        else:
            j=j-1
    if flag==1:
        print("Accepted")
    else:
        print("Rejected")
