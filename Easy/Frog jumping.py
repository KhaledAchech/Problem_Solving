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

# input
while 1:
    t = int(input())
    if t >= 1 and t <= 1000:
        break

# number of trials for each tiral we have moves (a and b) and jumps k
for i in range(t):
    x = 0
    # reading the moves
    while 1:
        a, b, k = map(int, sys.stdin.readline().split())
        if ((a >= 0 and a <= pow(10, 9)) and (b >= 0 and b <= pow(10, 9)) and (k >= 0 and k <= pow(10, 9))):
            break
    """
    if the number of moves are equal and the number of jumps is an even number
    the position will always stay the same
    """
    if a == b and k % 2 == 0:
        x = 0
    else:
        """
        if the number of moves are equal and the number of jumps is an odd number
        the position will change to 1 
        """
        if a == b and k % 2 == 1:
            x = 1
        else:
            # finding the new position
            for j in range(k):
                if j % 2 == 0:
                    x = x + a
                else:
                    x = x - b
            

    print(x)
