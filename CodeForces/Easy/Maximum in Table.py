"""
An n × n table a is defined as follows:

The first row and the first column contain ones, that is: a i, 1 = a 1, i = 1 for all i = 1, 2, ..., n.
Each of the remaining numbers in the table is equal to the sum of the number above it and the number to the left of it. In other words, the remaining elements are defined by the formula a i, j = a i - 1, j + a i, j - 1.
These conditions define all the values in the table.

You are given a number n. You need to determine the maximum value in the n × n table defined by the rules above.

Input
The only line of input contains a positive integer n (1 ≤ n ≤ 10) — the number of rows and columns of the table.

Output
Print a single line containing a positive integer m — the maximum value in the table.

"""
"""
#one way
import numpy as np

while True:
    n = int(input())
    if n >= 1 and n <= 10:
        break

#initializing the matrix
a = np.zeros((n,n),int)

#filling the a[i][1] and a[1][i] elements of the matrix
for x in range(n):
    a[x][0] = a[0][x] = 1

#filling the rest of the matrix
for x in range(1, n):
    for y in range(1, n):
        a[x][y] = a[x-1][y] + a[x][y-1]


m = np.max(a)
print(m)
"""
#the other way
while True:
    n = int(input())
    if n >= 1 or n <= 10:
        break

#initializing the set
a = [[0]*n]*n

#filling the a[i][1] and a[1][i] elements of the set
for x in range(n):
    a[x][0] = a[0][x] = 1

#filling the rest of the set
for x in range(1, n):
    for y in range(1, n):
        a[x][y] = a[x-1][y] + a[x][y-1]


#print(a.max())
m = max(max(x) for x in a)
print(m)
