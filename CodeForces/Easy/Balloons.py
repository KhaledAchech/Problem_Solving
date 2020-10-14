"""
In many contests, balloons are used to indicate to contestants the general state of the contest. Each time a team solves a problem, a balloon of a specific color is sent to the team and attached on or near their machine. As the contest progresses, the contest floor gradually fills up with a multi-colored display showing how various teams are doing in the contest.

Consider a contest of n problems in which each problem is attached to a specific balloon color. You will be able to see the balloon color of a problem in the contest floor if at least one team solved it during the contest.

You are given the number of accepted solutions on each problem. Your task is to count how many different colors you will be able to see. Can you?

Input
The first line contains an integer T (1 ≤ T ≤ 1000), in which T is the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 20), in which n is the number of problems in the contest.

Then a line follows containing n integers p1, p2, ..., pk (0 ≤ pi ≤ 100), in which pi is the number of accepted solutions on the ith problem.

Output
For each test case, print a single line containing the number different colors will you be able to see in the contest's floor.
"""
import sys

#inputs
t = int(input())

for i in range(t):
	n = int(input())
	a = list(map(int, sys.stdin.readline().split()))
	cp = 0 # ==> ballons counter for each test :)
	for i in range(len(a)):
		if a[i] != 0:
			cp += 1
	print(cp)
