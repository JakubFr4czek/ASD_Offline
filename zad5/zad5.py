from zad5testy import runtests
from collections import deque
from math import inf

#Jakub Fraczek
#Zlozonosc: O(V + E + E * log(V))
#O(E* log(V)) - zlozonosc algorytmu Dijkstry

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapifyMin(T, pos, N):

    l = left(pos)
    r = right(pos)

    mini = pos

    if l < N and T[l][1] < T[mini][1]:
        mini = l

    if r < N and T[r][1] < T[mini][1]:
        mini = r
    
    if mini != pos:
        T[pos], T[mini] = T[mini], T[pos]
        heapifyMin(T, mini, N)

def Dijkstra(G, v, n, b): 
    distance = [inf for _ in range(len(G))]
    distance[v] = 0

    queue = deque()

    queue.append((v,0))

    while len(queue) > 0:

        temp = queue.popleft()
        temp = temp[0]

        for i in range(len(G[temp])):

            if(distance[temp] + G[temp][i][1] < distance[G[temp][i][0]]):

                if distance[G[temp][i][0]] == inf:
                    queue.append((G[temp][i][0], distance[temp] + G[temp][i][1]))
                    heapifyMin(queue, 0, len(queue))

                distance[G[temp][i][0]] = distance[temp] + G[temp][i][1]

    if distance[b] == inf: return None


    return distance[b]

def spacetravel( n, E, S, a, b ):
    
    G = [[] for _ in range(n + 1)]

    for i in range(len(S)):
        G[S[i]].append((n, 0))
        G[n].append((S[i], 0))


    for i in range(len(E)):
        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][0], E[i][2]))

    return Dijkstra(G, a, n, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True)