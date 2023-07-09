from zad9testy import runtests
from queue import PriorityQueue

def Dijkstra(G, v):

    distance = [float('inf') for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0, v))

    while not queue.empty():

        priotity, temp = queue.get()

        for i in range(len(G[temp])):

            if distance[G[temp][i][0]] > priotity + G[temp][i][1]:
                distance[G[temp][i][0]] = priotity + G[temp][i][1]
                queue.put((distance[G[temp][i][0]], G[temp][i][0]))
                path[G[temp][i][0]] = temp
    #print(path)
    return distance


def min_cost(O, C, T, L):

    K = []

    for i in range(len(O)):
        K.append( (O[i],C[i]) )

    K.sort()
    K.append( (L,0) )

    #print(K)

    G = [ [] for i in range(len(K) * 2) ]

    for i in range(len(K)):

        pos, cost = K[i]

        j = i + 1

        while j < len(K) and K[j][0] < pos + T:

            G[2*i].append( (2 * j, K[j][1]) )
            G[2 * i + 1].append( (2 * j + 1, K[j][1]) )

            j += 1

        while j < len(K) and K[j][0] < pos + 2*T:

            G[2 * i].append( (2 * j + 1, K[j][1]) )

            j += 1

    G.append( [(0,0), (1,0)] ) #s

    #for i in range(len(G)):
    #    print(G[i])

    dist = Dijkstra(G, len(G) - 1)

    return(min(dist[len(dist) - 3], dist[len(dist) - 2]))





O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

#print(min_cost(O,C,T,L))

runtests( min_cost, all_tests = True )
