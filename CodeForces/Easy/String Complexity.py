"""
Let's call the complexity of a string to be the number of distinct letters in it. For example, the string "string" has complexity 6 and the string "letter" has complexity 4.

You like strings which have complexity either 1 or 2. Your friend has given you a string and you want to turn it into a string that you like. You have a magic eraser which will delete one letter from any string. Compute the minimum number of times you will need to use the eraser to turn the string into a string with complexity at most 2

Input
First line contains a single integer n ( 2≤n≤10^5 ) denoting the length of the string S.

Second line contains the string S that consists only of lowercase characters.

Output
Print one line containing one single integer denoting the minimum number of times you will need to use the eraser to turn the string into a string with complexity at most 2.
"""

#inputs 
n = int(input())
s = input()

#cleaning the string
ss = set(s)
#so we can organise the letters with their occurance
d = {}
for x in ss:
	d[x] = s.count(x)

#extracting the two letters with the most occurances
l =list(d.values())
c1 = max(l)
l.remove(c1)
c2 = max(l)

#figuring out how many letters were erased from the string 
x = c1 + c2
e = n - x
#output
print(e)
