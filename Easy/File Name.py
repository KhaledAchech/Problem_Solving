"""
You can not just take the file and send it. When Polycarp trying to send a file in the social network "Codehorses", he encountered an unexpected problem. If the name of the file contains three or more "x" (lowercase Latin letters "x") in a row, the system considers that the file content does not correspond to the social network topic. In this case, the file is not sent and an error message is displayed.

Determine the minimum number of characters to remove from the file name so after that the name does not contain "xxx" as a substring. Print 0 if the file name does not initially contain a forbidden substring "xxx".

You can delete characters in arbitrary positions (not necessarily consecutive). If you delete a character, then the length of a string is reduced by 1. For example, if you delete the character in the position 2 from the string "exxxii", then the resulting string is "exxii".

Input
The first line contains integer n (3≤n≤100) — the length of the file name.

The second line contains a string of length n consisting of lowercase Latin letters only — the file name.

Output
Print the minimum number of characters to remove from the file name so after that the name does not contain "xxx" as a substring. If initially the file name dost not contain a forbidden substring "xxx", print 0.
"""
#inputs
n = int(input())
s = input()

#initializing x : x_counter and i : iteration_counter
x = 0
i = 0
	
	
#specific case so we don't loop for unecessary reasons
#i ve noticed that if the string is containing only x's
#then x will be n(length of the string 's') - 2
if 'x'*n == s : 
	x = n - 2
#another specification where if there s no 'xxx' in the whole string
#then we ll go ahead and give x the 0 value :)
elif s.count('xxx') == 0:
	x = 0
else:
#the actual work start here :)
#the loop will go on until there is no more 'xxx' in s
	while s.count('xxx') != 0:
	#each new time the loop will go on i will be initialized  
		i = 0
		while i!=len(s):
				#sub will hold every 3 characters of the string
				sub = s[i:i+3]
				#now sub will be compared to 'xxx' if they are equal
				#then we ll need to leave one 'x' behind and increment the x value :)
				if sub == 'xxx':
					s = s[i+1:n]
					x += 1
				#then reinitialize i as the length of s has changed
					i = 0
				else:
				#else we ll just increment i to get another sub in the next loop :)
					i += 1


#printing the result :)
print(x)

