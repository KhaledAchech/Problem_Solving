"""
You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.

A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.

Input
The first line contains single positive integer n (1 ≤ n ≤ 10^5) — the number of integers.

The second line contains n positive integers a 1, a 2, ..., a n (1 ≤ a i ≤ 10^9).

Output
Print the maximum length of an increasing subarray of the given array.
"""
import sys

#input
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

#initializing the counter and the save 'x' variables
cnt = 0
x = 0

for i in range(n-1):
	if arr[i] < arr[i+1]:
		cnt += 1
	else:
		cnt += 1
		if cnt > x :
			x = cnt
		cnt = 0

#checking the corner case of having 1 value in 'arr'
#and checking if the last value is bigger than the one before
if arr[n-1] > arr[n-2] or n == 1:
	cnt += 1
	if cnt > x:
		x = cnt

#output
print(x)
