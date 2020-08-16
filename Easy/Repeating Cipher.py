"""
Polycarp loves ciphers. He has invented his own cipher called repeating.

Repeating cipher is used for strings. To encrypt the string s=s1s2…sm (1≤m≤10), Polycarp uses the following algorithm:

he writes down s1 ones,
he writes down s2 twice,
he writes down s3 three times,
...
he writes down sm m times.
For example, if s="bab" the process is: "b" → "baa" → "baabbb". So the encrypted s="bab" is "baabbb".

Given string t — the result of encryption of some string s. Your task is to decrypt it, i. e. find the string s.

Input
The first line contains integer n (1≤n≤55) — the length of the encrypted string. The second line of the input contains t — the result of encryption of some string s. It contains only lowercase Latin letters. The length of t is exactly n.

It is guaranteed that the answer to the test exists.

Output
Print such string s that after encryption it equals t.
"""
#inputs
n = int(input())
t = input()
 
s =''
i = 0
while i < len(t):
	x = len(t[i]*(i+1))
	if x == 1:
		s += t[i]
		i += 1
		pass
	if x == i+1:
		s += t[i]
		i = i + x
 
s_crypt=''
for i in range(len(s)):
	s_crypt += s[i]*(i+1)
 
if (s_crypt==t):
	print(s) 
 