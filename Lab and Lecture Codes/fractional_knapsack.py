def knapSack(W, wt, val, n):
    gain = 0
    ratio = [0 for i in range(n)]

    for i in range(n):
        ratio[i] = val[i] / wt[i]

    zipped = zip(ratio, val, wt)
    zipped = sorted(list(zipped), reverse=True)

    for i in range(n):
        if zipped[i][2] <= W:
            gain += zipped[i][1]
            W -= zipped[i][2]

    return gain


price = [10, 5, 3, 2, 8, 7, 11]
weight = [2, 3, 1, 4, 3, 2, 7]
W = 5
n = 7

print(knapSack(W, weight, price, n))
