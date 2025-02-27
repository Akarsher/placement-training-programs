''' High school student Vasya got a string of length n as a birthday present. This string consists of letters 'a' and 'b' only. Vasya denotes beauty of the string as the maximum length of a substring (consecutive subsequence) consisting of equal letters.

Vasya can change no more than k characters of the original string. What is the maximum beauty of the string he can achieve?

Input
The first line of the input contains two integers n and k (1 ≤ n ≤ 100 000, 0 ≤ k ≤ n) — the length of the string and the maximum number of characters to change.

The second line contains the string, consisting of letters 'a' and 'b' only.

Output
Print the only integer — the maximum beauty of the string Vasya can achieve by changing no more than k characters.'''

def max_beauty(n, k, s):
    def max_length(char):
        left = 0
        count = 0
        max_len = 0
        for right in range(n):
            if s[right] != char:
                count += 1
            while count > k:
                if s[left] != char:
                    count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
    
    max_a = max_length('a')
    max_b = max_length('b')
    
    return max(max_a, max_b)

n, k = map(int, input().split())
s = input().strip()

result = max_beauty(n, k, s)

print(result)
