import math
def ceil(a,b):
    r = a // b
    if a % b > 0:
        r += 1
    return r
def solution(M, F):
    a, b = int(M), int(F)
    cnt = 0
    while a != b:
        if a < b:
            a, b = b, a
        add = ceil((a - b),b)
        cnt += add
        a -= add * b
    ans = "impossible"
    if a == 1 and b == 1:
        ans = str(cnt) 
    return ans

print(solution('7','4'))