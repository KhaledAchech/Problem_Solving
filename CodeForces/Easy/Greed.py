"""
Jafar has n cans of cola. Each can is described by two integers: remaining volume of cola ai and can's capacity bi (ai  ≤  bi).

Jafar has decided to pour all remaining cola into just 2 cans, determine if he can do this or not!

Input
The first line of the input contains one integer n (2 ≤ n ≤ 100 000) — number of cola cans.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 109) — volume of remaining cola in cans.

The third line contains n space-separated integers that b1, b2, ..., bn (ai ≤ bi ≤ 109) — capacities of the cans.

Output
Print "YES" (without quotes) if it is possible to pour all remaining cola in 2 cans. Otherwise print "NO" (without quotes).

You can print each letter in any case (upper or lower).
"""
import sys

#input
n = int(input())
rem = list(map(int, sys.stdin.readline().split()))
cap = list(map(int, sys.stdin.readline().split()))

x = sum(rem) # ==> sum of all the remaining cola 
m1= cap.pop(cap.index(max(cap))) # the 1st can with maximum capacity 
m2= cap.pop(cap.index(max(cap))) # the 2nd can with maximum capacity
m = m1+m2 # ==> summing the cans capacity


#output
if x <= m:
	print('YES')
else:
	print('NO')