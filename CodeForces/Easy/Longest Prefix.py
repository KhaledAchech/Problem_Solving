"""
You are given two strings a and b. Find the longest common prefix between them after performing zero or more operation on string b. In each operation you can swap any two letters.

Input
The first line of the input contains an integer T (1 ≤ T ≤ 500), where T is the number of the test cases.

Each case has one line that contains two space separated strings a and b.

All strings are non-empty consisting of lowercase English letters only. The length of each of these strings does not exceed 105 characters.

Output
Print T lines, each line contains a single integer that represents the length of the longest common prefix between a and b.
"""
import sys
#input
t = int(input())

for i in range(t):
	a, b = map(str, sys.stdin.readline().lower().split())
	
	

