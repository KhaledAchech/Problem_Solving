"""
TEK-UP is hosting an event this week, D participants will attend the event. However it's decided that the event has to take place in only one of the classrooms.

There are N classrooms, each classroom has a capacity of Ai persons. Since it's a training week at TEK-UP, not all the classrooms are free. Classrooms are numbered from 1 to N. We know that all the classrooms from L to R (inclusive) are empty and can be used to host the event.

We are asking for your help to know how many free classrooms can be used to host the event containing at least D participants .

Input
First line of input contains three integers N and D ( 1≤N≤105 , 1≤D≤109 ) denoting the number of classrooms and the number of participants respectively.

Next line contains N space separated integers Ai ( 1≤Ai≤109) denoting the capacity of the i−th classroom.

One line follows containing 2 integers L and R ( 1≤L≤R≤n ) denoting free classrooms.

Output
Print a single integer, the number of free classrooms that could host the event given the number of participants.
"""
import sys

#inputs
n, d = (map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
l, r = (map(int, sys.stdin.readline().split()))

#the l value substracted by 1 because the array 'a' starts from 0 :)
l -= 1 

#initializing the empty classroom counter :)
cp = 0

for i in range(l,r):
	if a[i] >= d:
		cp += 1

#output
print(cp) 
