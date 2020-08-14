
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
def main():
	def read_tests():
		while 1:
			t = int(input())
			if t >= 1 and t <= 1000:
				return t
			else:
				return read_tests()

	def verify(x):
		r = range(1, 10**9+1)
		if x not in r:
			return False
		else:
			return True

	def inputs():
			 dict={}
			 a, b, k = map(int, sys.stdin.readline().split())
			 if verify(a) and verify(b) and verify(k):
			 	return {'a': a, 'b': b, 'k': k}
			 else:
			 	return inputs()

	def find_new_position(a, b, k):
		    val = 0
		    if a == b and k % 2 == 0:
		        return 0
		    elif a == b and k % 2 == 1:
		    	return 1
		    else:
		    	if k % 2 == 1: 
		    		val = (a * (k//2)) - (b * (k//2)) + a
		    	else:
		    		val = (a * k//2) - (b * k//2)
		    	return val


	t = read_tests()

	def exec():
		input_dict = inputs()
		a = input_dict.get('a')
		b = input_dict.get('b')
		k = input_dict.get('k')
		x = find_new_position(a,b,k)
		sys.stdout.write(str(x))
		sys.stdout.write('\n')


	res = {exec() for i in range(t)}
		
main()




		

