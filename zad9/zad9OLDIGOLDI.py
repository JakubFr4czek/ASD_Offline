from zad9testy import runtests
from queue import PriorityQueue


def min_cost(O, C, T, L):
    n = len(O)
    dp = [float('inf')] * (n + 2)
    dp[0] = 0
    for i in range(1, n + 2):
        for j in range(i):
            if (i == n + 1 and L - O[j - 1] <= T) or (i != n + 1 and O[i - 1] - O[j - 1] <= T) or (O[i - 1] - O[j - 1] <= 2 * T and j == 0):
                dp[i] = min(dp[i], dp[j] + (C[i - 1] if i != n + 1 else 0))
    return dp[n + 1]



O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

#print(min_cost(O, C, T, L))

runtests( min_cost, all_tests = True )
