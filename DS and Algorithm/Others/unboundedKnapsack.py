W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)


def knapSack(W, wt, val, n):
    t = [[float("-inf") for _ in range(W+1)] for _ in range(n+1)]
    for i in range(W+1):
        t[0][i] = 0
    for i in range(n+1):
        t[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[-1][-1]


print(knapSack(W, wt, val, n))
