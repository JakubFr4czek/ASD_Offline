from zad9testy import runtests
from queue import PriorityQueue


def min_cost( O, C, T, L ):

    dq = []
    pq = PriorityQueue()

    for i in range(len(O)):

        dq.append( (O[i], C[i]) ) #sortuje po dystansie rosnaco

    dq.sort()
    #print(dq)
    pos = 0 #Pozycja w tablicy dq

    while pos < len(dq) and dq[pos][0] <= 2*T:

        if dq[pos][0] <= 0 + T: #Najpierw sie bedzie wykonywac to
            pq.put( (0 + dq[pos][1],  dq[pos][0], False, pos + 1) ) # (koszt, pozycja kierowcy, czy_wykorzystano_nadgodziny)
        elif dq[pos][0] <= 0 + 2*T:
            pq.put( (dq[pos][1], dq[pos][0], True, pos + 1) ) #Potem to

        pos += 1

    while not pq.empty():

        cost, driverPos, overtime, pos = pq.get()
        #print(cost, driverPos, overtime, pos - 1, " | ",parentInfo)
        #parentInfo = "" + str(cost) + " " + str(driverPos) + " " + str(overtime) + " " + str(pos - 1)

        if driverPos + T >= L:
            return cost
        elif overtime == False:
            if driverPos + 2*T >= L:
                return cost

        while pos < len(dq) and dq[pos][0] <= driverPos + 2*T:

            if dq[pos][0] <= driverPos + T:
                pq.put( (cost + dq[pos][1], dq[pos][0], overtime, pos + 1) )
            elif dq[pos][0] <= driverPos + 2*T and overtime == False:
                pq.put( (cost + dq[pos][1], dq[pos][0], True, pos + 1) )
            
            pos += 1

    return -1

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

#print(min_cost(O, C, T, L))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
