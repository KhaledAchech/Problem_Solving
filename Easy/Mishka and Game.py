"""
Mishka and Game

Mishka is a little polar bear. As known, little bears loves spending their free time playing dice for chocolates. Once in a wonderful sunny morning, walking around blocks of ice, Mishka met her friend Chris, and they started playing the game.

Rules of the game are very simple: at first number of rounds n is defined. In every round each of the players throws a cubical dice with distinct numbers from 1 to 6 written on its faces. Player, whose value after throwing the dice is greater, wins the round. In case if player dice values are equal, no one of them is a winner.

In average, player, who won most of the rounds, is the winner of the game. In case if two players won the same number of rounds, the result of the game is draw.

Mishka is still very little and can't count wins and losses, so she asked you to watch their game and determine its result. Please help her!

Input
The first line of the input contains single integer n n (1 ≤ n ≤ 100) — the number of game rounds.

The next n lines contains rounds description. i-th of them contains pair of integers m i and c i (1 ≤ m i,  c i ≤ 6) — values on dice upper face after Mishka's and Chris' throws in i-th round respectively.

Output
If Mishka is the winner of the game, print "Mishka" (without quotes) in the only line.

If Chris is the winner of the game, print "Chris" (without quotes) in the only line.

If the result of the game is draw, print "Friendship is magic!^^" (without quotes) in the only line.

"""
import sys

while True:
    x = int(input())
    if x >= 1 or x <= 100:
        break

Mishka_score = 0
Chris_score = 0
# for each round Mishka and Chris will throw the dice
for i in range(x):
    #trowing the dice
    while True:
        m, c = map(int, sys.stdin.readline().split())
        if ((m >= 1 or m <= 6) and (c >= 1 or c <= 6)):
            break

    # comparing the dice rolls
    if m > c:
        Mishka_score += 1

    if c > m:
        Chris_score += 1

    if c == m:
        Mishka_score += 1
        Chris_score += 1

# comparing the scores and seeing who is the winner
if Mishka_score > Chris_score:
    print('Mishka')

if Chris_score > Mishka_score:
    print('Chris')

if Mishka_score == Chris_score:
    print('Friendship is magic!^^')

