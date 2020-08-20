"""
You are locked in a room with a door that has a keypad with 10 keys corresponding to digits from 0 to 9. To escape from the room, you need to enter a correct code. You also have a sequence of digits.

Some keys on the keypad have fingerprints. You believe the correct code is the longest not necessarily contiguous subsequence of the sequence you have that only contains digits with fingerprints on the corresponding keys. Find such code.

Input
The first line contains two integers n and m (1≤n,m≤10) representing the number of digits in the sequence you have and the number of keys on the keypad that have fingerprints.

The next line contains n distinct space-separated integers x1,x2,…,xn (0≤xi≤9) representing the sequence.

The next line contains m distinct space-separated integers y1,y2,…,ym (0≤yi≤9) — the keys with fingerprints.

Output
In a single line print a space-separated sequence of integers representing the code. If the resulting sequence is empty, both printing nothing and printing a single line break is acceptable.
"""
import sys

#inputs:
n, m = map(int, sys.stdin.readline().split())
n_sequences = input()
m_fingerprints = input()

#initializing code the result string to empty.
code = ''

#figuring out the code.
for i in range(len(n_sequences)):
	if n_sequences[i] != " " and n_sequences[i] in m_fingerprints:
		code = code + ' ' + n_sequences[i]

print(code)