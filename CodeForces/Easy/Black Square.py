"""
Quite recently, a very smart student named Jury decided that lectures are boring, so he downloaded a game called "Black Square" on his super cool touchscreen phone.

In this game, the phone's screen is divided into four vertical strips. Each second, a black square appears on some of the strips. According to the rules of the game, Jury must use this second to touch the corresponding strip to make the square go away. As Jury is both smart and lazy, he counted that he wastes exactly a i calories on touching the i-th strip.

You've got a string s, describing the process of the game and numbers a 1, a 2, a 3, a 4. Calculate how many calories Jury needs to destroy all the squares?

Input
The first line contains four space-separated integers a 1, a 2, a 3, a 4 (0 ≤ a 1, a 2, a 3, a 4 ≤ 104).

The second line contains string s (1 ≤ |s| ≤ 105), where the і-th character of the string equals "1", if on the i-th second of the game the square appears on the first strip, "2", if it appears on the second strip, "3", if it appears on the third strip, "4", if it appears on the fourth strip.

Output
Print a single integer — the total number of calories that Jury wastes.
"""
import sys

#inputs 
a1, a2, a3, a4 = map(int, sys.stdin.readline().split())
s = input()

#result value
res = 0

"""
first way of getting the result with a time complexity of O(n)
for i in range(len(s)):
	if s[i] == '1':
		res += a1

	if s[i] == '2':
		res += a2

	if s[i] == '3':
		res += a3

	if s[i] == '4':
		res += a4

"""
#second way with a time complexity of O(1)
res += s.count('1')*a1 + s.count('2')*a2 + s.count('3')*a3 + s.count('4')*a4
print(res)