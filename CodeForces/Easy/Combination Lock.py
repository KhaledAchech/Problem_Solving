"""
Scrooge McDuck keeps his most treasured savings in a home safe with a combination lock. Each time he wants to put there the treasures that he's earned fair and square, he has to open the lock.
The combination lock is represented by n rotating disks with digits from 0 to 9 written on them. Scrooge McDuck has to turn some disks so that the combination of digits on the disks forms a secret combination.
In one move, he can rotate one disk one digit forwards or backwards. In particular, in one move he can go from digit 0 to digit 9 and vice versa. What minimum number of actions does he need for that?
Input
The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of disks on the combination lock.

The second line contains a string of n digits — the original state of the disks.

The third line contains a string of n digits — Scrooge McDuck's combination that opens the lock.

Output
Print a single integer — the minimum number of moves Scrooge McDuck needs to open the lock.
"""
import sys

#inputs
n = int(input())
o_lock = input()
code = input()

#Initializing the number of moves.
mo = 0

#Initializing the loop counter
i = 0
while i < len(o_lock):
	#Converting the i^th character into an int
	lock = int(o_lock[i])
	co = int(code[i])

	#if the difference between the lock and the code is bigger than five than
	#we ll have to decide if we need to go ahead exp: lock = 7 then we increment to 9
	#or we retreat back to zero 
	if abs(lock - co) > 5:
		if lock < 5: # ==> making the decision
			mo += lock + (9 - co) + 1 
		else:
			mo += (9 - lock) + co + 1
	else:
		#else we just add up the difference to our moves counter 
		mo += abs(lock - co)
	i += 1


#Output
print(mo)
