"""
The Saratov State University Olympiad Programmers Training Center (SSU OPTC) has n students. For each student you know the number of times he/she has participated in the ACM ICPC world programming championship. According to the ACM ICPC rules, each person can participate in the world championship at most 5 times.

The head of the SSU OPTC is recently gathering teams to participate in the world championship. Each team must consist of exactly three people, at that, any person cannot be a member of two or more teams. What maximum number of teams can the head make if he wants each team to participate in the world championship with the same members at least k times?

Input
The first line contains two integers, n and k (1 ≤ n ≤ 2000; 1 ≤ k ≤ 5). The next line contains n integers: y 1, y 2, ..., y n (0 ≤ y i ≤ 5), where y i shows the number of times the i-th person participated in the ACM ICPC world championship.

Output
Print a single number — the answer to the problem.
"""
import sys

#inputs
n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

#filtring the participants by their number of participations 
#and if their number of participations is going to become > 5 then we don't pick them.
part = [l[i] for i in range(len(l)) if l[i] != 5 and l[i]+k <= 5]


#possible numbers of teams we can forme from these participants 
res = len(part)//3

print(res)