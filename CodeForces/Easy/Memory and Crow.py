"""
There are n integers b1, b2, ..., bn written in a row. For all i from 1 to n, values ai are defined by the crows performing the following procedure:

The crow sets ai initially 0.
The crow then adds bi to ai, subtracts bi + 1, adds the bi + 2 number, and so on until the n'th number. Thus, ai = bi - bi + 1 + bi + 2 - bi + 3....
Memory gives you the values a1, a2, ..., an, and he now wants you to find the initial numbers b1, b2, ..., bn written in the row? Can you do it?

Input
The first line of the input contains a single integer n (2 ≤ n ≤ 100 000) — the number of integers written in the row.

The next line contains n, the i'th of which is ai ( - 109 ≤ ai ≤ 109) — the value of the i'th number.

Output
Print n integers corresponding to the sequence b1, b2, ..., bn. It's guaranteed that the answer is unique and fits in 32-bit integer type.
"""
import sys
#input 
n = int(input())
l = list(map(int, sys.stdin.readline().split()))

#making of the empty list result
res = [0]*n

res[n-1] = l[n-1]# ==> last element of the list stays the same
i = n-2 # ==> starting from the element right before the last element of the list 

#loop backwards and adding the elements to find the initial value.
while i >= 0:
	res[i] += l[i]+l[i+1]
	i-=1

#output
print(' '.join(map(str, res)))