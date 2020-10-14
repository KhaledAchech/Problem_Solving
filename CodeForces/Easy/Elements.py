"""
Mohsen woke up late, his phone ran out of battery so it got shut down and didn't ring. He packed his things fast and left in a hurry.

After leaving home, he remembered he only took n elements that he left on his desk and he doesn't know whether the element with the value k is one of the elements on the desk or not. Unfortunately for him, he needs that element today in school so he has to check all the n elements he took but that would take so much time.

Mohsen needs your help to tell him whether he took that element or not.

Input
First line of input contains 2 integers n and k ( 1 ≤ n ≤ 105 , 1 ≤ k ≤ 1000 ) denoting the number of elements and the value of the element Mohsen is looking for.

Second line contains n space separated integers Ai ( 1 ≤ Ai ≤ 1000 ) where Ai is the value of the i'th element.

Output
Print "YES" if the element with value k is one of the n elements, otherwise print "NO".
"""
import sys

#inputs
n, k = (map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

if k in a:
	print('YES')
else:
	print('NO')
