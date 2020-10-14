"""
A group of junior programmers are attending an advanced programming camp, where they learn very difficult algorithms and programming techniques! Near the center in which the camp is held, is a professional bakery which makes tasty pastries and pizza. It is called 'Bonabity'... or 'Ponapety'... or 'Ponabity'... Actually no one knows how to spell this name in English, even the bakery owner doesn't, and the legends say that Arabs always confuse between 'b' and 'p', and also between 'i' and 'e', so 'b' for them is just the same as 'p', and 'i' for them is just the same as 'e', they also don't care about letters' cases (uppercase and lowercase for a certain letter are similar). For example, the words 'Ponabity' and 'bonabety' are considered the same. You are given two words including only upper case and lower case English letters, and you have to determine whether the two words are similar in Arabic.

Input
The input consists of several test cases. The first line of the input contains a single integer T, the number of the test cases. Each of the following T lines represents a test case and contains two space-separated strings (each one consists of only upper case and lower case English letters and its length will not exceed 100 characters).

Output
For each test case print a single line: 'Yes' if the words are similar in Arabic and 'No' otherwise.

"""
import sys

#inputs
t = int(input())

for i in range(t):
	w1,w2 = map(str, sys.stdin.readline().lower().split())
	if len(w1) != len(w2):
		print('No')
	else:
		if 'b' in w1:					# so this is a slight tweek	
			w1 = w1.replace('b','p') 	# basicaly the algorithme will
		if 'e' in w1:					# change the two words	
			w1 = w1.replace('e','i')	# by transforming all the 'b's
		if 'b' in w2:					# into 'p's and all the 'e's 
			w2 = w2.replace('b','p')	# into 'i's
		if 'e' in w2:					# then we campare the two words
			w2 = w2.replace('e','i')	# if they re equal then they are
										# the same.
		# Output ^^
		if w1 == w2 :					
			print('Yes')
		else:
			print('No')
