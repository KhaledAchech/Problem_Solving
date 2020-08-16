import 
def solution(n):
    q = queue.Queue()
    d = {}
    n = int(n)
    d[n] = 0
    q.put(n)
    while (not q.empty()):
        x = q.get()
        if (x == 1):
            return d[x]
        if (x % 2 == 0):
            d[x // 2] = d[x] + 1
            q.put(x // 2)
        else:
            if x + 1 not in d:
                q.put(x + 1)
                d[x + 1] = d[x] + 1
            if x - 1 not in d:
                d[x - 1] = d[x] + 1 
                q.put(x - 1)


print (solution('15'))