"""
A frog is currently at the point 0 on a coordinate axis Ox. It jumps by the following algorithm: the first jump is a units to the right, the second jump is b units to the left, the third jump is a units to the right, the fourth jump is b units to the left, and so on.

Formally:

if the frog has jumped an even number of times (before the current jump), it jumps from its current position x to position x+a;
otherwise it jumps from its current position x to position x−b.
Your task is to calculate the position of the frog after k jumps.

But... One more thing. You are watching t different frogs so you have to answer t independent queries.

Input
The first line of the input contains one integer t (1≤t≤1000) — the number of queries.

Each of the next t lines contain queries (one query per line).

The query is described as three space-separated integers a,b,k (1≤a,b,k≤109) — the lengths of two types of jumps and the number of jumps, respectively.

Output
Print t integers. The i-th integer should be the answer for the i-th query.
"""
import sys

#this function will help us find the new position of the frog
def find_new_position(a, b, k):
	#if all the moves are equal and the number of jumps is an even number the position will stay the same 
	if k % 2 == 0:
			return (a * (k//2)) - (b * (k//2))	

	#the same except the number of jumps is an odd number
	elif k % 2 == 1:
			return (a * (k//2)) - (b * (k//2)) + a

t = int(input())

#for each test will figure out the new positions of the frogs :)
for i in range(t):	
	a, b, k = map(int, sys.stdin.readline().split())   	
	x = find_new_position(a,b,k)
	sys.stdout.write(str(x))
	sys.stdout.write('\n')
