"""
Bizon the Champion is called the Champion for a reason.

Bizon the Champion has recently got a present — a new glass cupboard with n shelves and he decided to put all his presents there. All the presents can be divided into two types: medals and cups. Bizon the Champion has a 1 first prize cups, a 2 second prize cups and a 3 third prize cups. Besides, he has b 1 first prize medals, b 2 second prize medals and b 3 third prize medals.

Naturally, the rewards in the cupboard must look good, that's why Bizon the Champion decided to follow the rules:

any shelf cannot contain both cups and medals at the same time;
no shelf can contain more than five cups;
no shelf can have more than ten medals.
Help Bizon the Champion find out if we can put all the rewards so that all the conditions are fulfilled.

Input
The first line contains integers a 1, a 2 and a 3 (0 ≤ a 1, a 2, a 3 ≤ 100). 
The second line contains integers b 1, b 2 and b 3 (0 ≤ b 1, b 2, b 3 ≤ 100). 
The third line contains integer n (1 ≤ n ≤ 100).

The numbers in the lines are separated by single spaces.

Output
Print "YES" (without the quotes) if all the rewards can be put on the shelves in the described manner. Otherwise, print "NO" (without the quotes).
"""
import sys
import math
#inputs
cups = list(map(int, sys.stdin.readline().split()))
medals = list(map(int, sys.stdin.readline().split()))
n = int(input())

#figuring out how many cups per shelf and how many medals per shelf
x = math.ceil(sum(cups)/5)
y = math.ceil(sum(medals)/10)

#output
if x + y <= n : 
	print ('YES')
else:
	print ('NO')



