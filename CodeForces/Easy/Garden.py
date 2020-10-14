"""
Luba thinks about watering her garden. The garden can be represented as a segment of length k. Luba has got n buckets, the i-th bucket allows her to water some continuous subsegment of garden of length exactly ai each hour. Luba can't water any parts of the garden that were already watered, also she can't water the ground outside the garden.

Luba has to choose one of the buckets in order to water the garden as fast as possible (as mentioned above, each hour she will water some continuous subsegment of length ai if she chooses the i-th bucket). Help her to determine the minimum number of hours she has to spend watering the garden. It is guaranteed that Luba can always choose a bucket so it is possible water the garden.

See the examples for better understanding.

Input
The first line of input contains two integer numbers n and k (1 ≤ n, k ≤ 100) — the number of buckets and the length of the garden, respectively.

The second line of input contains n integer numbers ai (1 ≤ ai ≤ 100) — the length of the segment that can be watered by the i-th bucket in one hour.

It is guaranteed that there is at least one bucket such that it is possible to water the garden in integer number of hours using only this bucket.

Output
Print one integer number — the minimum number of hours required to water the garden.
"""
import sys
#inputs
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

#getting the dividers of k
res = [a[i] for i in range(len(a)) if k % a[i]== 0]

#output
print(k // max(res))