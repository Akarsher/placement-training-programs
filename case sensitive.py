'''There is a string 
s
s of length 
3
3, consisting of uppercase and lowercase English letters. Check if it is equal to "YES" (without quotes), where each letter can be in any case. For example, "yES", "Yes", "yes" are all allowable.

Input
The first line of the input contains an integer 
t
t (
1
≤
t
≤
10
3
1≤t≤10 
3
 ) — the number of testcases.

The description of each test consists of one line containing one string 
s
s consisting of three characters. Each character of 
s
s is either an uppercase or lowercase English letter.'''

a=int(input())
for i in range(1,a+1):
  s=input().lower()
  if (s=="yes"):
     print("YES")
  else:
     print("NO")
