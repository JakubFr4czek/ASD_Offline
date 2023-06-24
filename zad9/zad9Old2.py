from zad9testy import runtests
from queue import PriorityQueue


def min_cost( O, C, T, L ):

    dp = []
    pq = PriorityQueue()

    for i in range(len(O)):

    dp.append( (O[i], C[i], float('inf'), float('inf')) ) #sortuje po dystansie rosnaco,  (dystans, koszt, kosztDostaniaT, kosztDostania2T)
    dp.append( (0, 0, 0, 0) )
    dp.append( (L, 0, float('inf'), float('inf')) )
    dp.sort()


    #print(dp)

    for i in range(len(dp)):

        truckPos, ParkingCost, TCost, T2Cost = dp[i]

        print(truckPos, ParkingCost, TCost, T2Cost)

        #if T2Cost < TCost and truckPos + T >= L:
        #    return T2Cost
        #elif T2Cost >= TCost and truckPos + 2*T >= L:
        #    return TCost

        j = i + 1

        

        while(j < len(dp) and dp[j][0] <= truckPos + T):

            if TCost + dp[j][1] < dp[j][2]:
                dp[j] = (dp[j][0], dp[j][1], TCost + dp[j][1], dp[j][3])

            if T2Cost + dp[j][1] < dp[j][3]:
                dp[j] = (dp[j][0], dp[j][1], dp[j][2], T2Cost + dp[j][1])

            if dp[j][2] < dp[j][3]:
                dp[j] = (dp[j][0], dp[j][1], dp[j][2], dp[j][2])      
            j+=1

            
        while(j < len(dp) and dp[j][0] <= truckPos + 2*T):

            if TCost + dp[j][1] < dp[j][3]:
                dp[j] = (dp[j][0], dp[j][1], dp[j][2], TCost + dp[j][1])
                    #print(dp[j])

            j+=1

    pos, cost, TCost, T2Cost = dp[len(dp) - 1]

    if TCost == float('inf') and T2Cost == float('inf'):
        return -1
    else:
        return min(TCost, T2Cost)

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

print(min_cost(O, C, T, L))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( min_cost, all_tests = True )
