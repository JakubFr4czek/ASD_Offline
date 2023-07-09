from zad7testy import runtests

def maze( L ):

    dp = [ [ 0 for j in range(len(L[i])) ] for i in range(len(L)) ]

    for i in range(len(L)):

        lewo = gora = dol = float('-inf')

        if i == 0:
            gora = 0
            lewo = 0

        #W dol
        for j in range(len(L[i])):

            if j - 1 >= 0:
                gora = dp[j - 1][i]
            if i - 1 >= 0:
                lewo = dp[j][i - 1]

            if L[j][i] == '#':
                dp[j][i] = float('-inf')
                if i == 0:
                    for k in range(j, len(L)):
                        dp[k][i] = float('-inf')
                    break
            else:
                dp[j][i] = max(lewo, gora) + 1

        #w gore

        

        if i == 0:
            continue
        
        dol = float('-inf')

        for j in range(len(L[i])-1, -1, -1):
            
            if i - 1 >= 0:
                lewo = dp[j][i - 1]

            if L[j][i] == '#':
                dp[j][i] = float('-inf')
                dol = float('-inf')
                continue
            else:
                dp[j][i] = max(dp[j][i], max(lewo, dol) + 1)

            dol = max(lewo, dol) + 1

    #for i in range(len(dp)):
#       print(dp[i])

    return dp[len(dp) - 1][len(dp) - 1] - 1





L = ['......', 
     '#..#..', 
     '.#..#.', 
     '##..#.', 
     '......', 
     '......']

print( maze( L ) )

runtests( maze, all_tests = True )
