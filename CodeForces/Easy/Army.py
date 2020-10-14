'''
The Berland Armed Forces System consists of n ranks that are numbered using natural numbers from 1 to n, where 1 is the lowest rank and n is the highest rank.

One needs exactly d i years to rise from rank i to rank i + 1. Reaching a certain rank i having not reached all the previous i - 1 ranks is impossible.

Vasya has just reached a new rank of a, but he dreams of holding the rank of b. Find for how many more years Vasya should serve in the army until he can finally realize his dream.

Input
The first input line contains an integer n (2 ≤ n ≤ 100). The second line contains n - 1 integers d i (1 ≤ d i ≤ 100). The third input line contains two integers a and b (1 ≤ a < b ≤ n). The numbers on the lines are space-separated.

Output
Print the single number which is the number of years that Vasya needs to rise from rank a to rank b.
'''
import sys
#input
n = int(input())
d = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
#adjusting the ranks order 
f_r = b - 1
c_r = a - 1

#result variable
s = 0

#initalizing counter
while c_r != f_r:
	s += d[c_r]
	c_r += 1

print(s) 
