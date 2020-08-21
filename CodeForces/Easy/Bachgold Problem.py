"""
Bachgold problem is very easy to formulate. Given a positive integer n represent it as a sum of maximum possible number of prime numbers. One can prove that such representation exists for any integer greater than 1.

Recall that integer k is called prime if it is greater than 1 and has exactly two positive integer divisors — 1 and k.

Input
The only line of the input contains a single integer n (2 ≤ n ≤ 100 000).

Output
The first line of the output contains a single integer k — maximum possible number of primes in representation.

The second line should contain k primes with their sum equal to n. You can print them in any order. If there are several optimal solution, print any of them.
"""

#inputs
n = int(input())

s = ''
if n % 2 == 0:
	x = int(n/2)
	s += x*'2 '
	l = x
else:
	y = n-3
	x = int(y/2)
	s += x*'2 ' + '3'
	l = x+1

print(l)
print(s)