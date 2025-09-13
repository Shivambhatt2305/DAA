# def coin(amt,coins):
#     T=[len(amt)+1]
#     for i in range(len(amt)):
#         for j in range(len(coins)):
#             if j <coins[i]:
#                 T[i][j]=T[i-1][j]
#             else:
#                 T[i][j]=min(T[i-1][j],1+T[i][j-coins[i]])
#     return T[n,amt]
    
# amt=[0,1,2,3,4,5,6,7,8,9,10,11]
# coins=[1,5,6,8]
# print(coin(amt,coins))

def coin(amt, coins):
    n = len(coins)
    m = max(amt)  # maximum amount
    T = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: 0 amount requires 0 coins
    for i in range(n + 1):
        T[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if coins[i - 1] <= j:
                T[i][j] = min(T[i - 1][j], 1 + T[i][j - coins[i - 1]])
            else:
                T[i][j] = T[i - 1][j]

    return T[n][amt[-1]] if T[n][amt[-1]] != float('inf') else -1


# Example usage
amt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
coins = [1, 5, 6, 8]
print(coin(amt, coins))  # Output: 2 (5 + 6)
