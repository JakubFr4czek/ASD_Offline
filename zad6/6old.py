from zad6testy import runtests
from collections import deque


def BFS(M, v):

    queue = deque()
    visited = [False for _ in range(len(M))]
    path = [-1 for _ in range(len(M))]

    queue.append(v)
    visited[v] = True 
    
    while(len(queue) > 0):

        temp = queue.popleft()

        for i in range(len(M[temp])):
            if M[temp][i] > 0 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                path[i] = temp
    #print(path)
    return path

def EdmondsKarp(M, s, t):

    flow = 0

    path = deque()
    path = BFS(M, s)

    while path[t] != -1:

        temp = t
        mini = float('inf')

        while temp != s:
            mini = min(mini, M[path[temp]][temp])
            temp = path[temp]
        temp = t

        while temp != s:
            M[path[temp]][temp] -= mini
            M[temp][path[temp]] += mini
            temp = path[temp]

        flow += mini

        path = BFS(M, s)
    return flow

def binworker( M ):

    #robie sobie z tego graf dwudzielny

    #Wejscie bedzie do wszystkich n workerow, a wyjscie od wszystkich maszyn

    inG = 2 * len(M)
    outG = 2 * len(M) + 1

    G = [ [0 for j in range(2* len(M) + 2)] for i in range(2* len(M) + 2)]

    for i in range(len(M)):
        for j in range(len(M[i])):
            G[M[i][j]][len(M) + i] = 1

    for i in range(len(M)):
        G[inG][i] = 1
        G[len(M) + i][outG] = 1

    for i in range(len(G)):
        print(G[i])

    return EdmondsKarp(G, inG, outG)


M = [ [ 0, 1, 3], # 5
[ 2, 4], # 6
[ 0, 2], # 7
[ 3 ], # 8
[ 3, 2] ] # 9


print(binworker( M ))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( binworker, all_tests = False )
