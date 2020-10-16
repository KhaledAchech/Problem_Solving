"""
Hasan and Hussain are playing a game with W × H paper, the game consist of turns; Hasan starts first.
On each turn, the player chooses one of the pieces of paper and cuts it into two papers such that 
the cut must be a straight line parallel to one of the paper sides and must cut the paper to two pieces 
of paper with integer dimensions.
The loser is the one who can't make a move (i.e when all pieces of paper become 1 × 1). Assuming that Hasan and Hussain are playing optimally, who will win the game?

Input
The first line of input is an integer T(1 ≤ T ≤ 101) which represents the number of test cases. Each of the next T lines consists of two space-separated integers W,H (1 ≤ W,H ≤ 100,000) the width and the height of the paper.

Output
For each test case, output a single line representing its answer; if Hasan is the winner output "Hasan" (without quotes) otherwise "Hussain" (without quotes).

"""

import sys

#inputs
t = int(input())



for i in range(t):
	w, h = map(int,sys.stdin.readline().split())
	m = (w * h) - 1
	if m % 2 == 0:
		print('Hussain')
	else:
		print('Hasan')