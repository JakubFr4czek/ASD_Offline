from zad6testy import runtests
from collections import deque

#Jakub Frączek
#O(VE)

'''
def BFS(G, s, t):

    visited = [False] * len(G)
    path = [(-1, -1)] * len(G)
    queue = deque()

    visited[s] = True
    queue.append(s)

    while len(queue) > 0:
        
        temp = queue.popleft()

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:

                path[G[temp][i]] = (temp,i)

                if G[temp][i] == t:
                    return path

                visited[G[temp][i]] = True
                queue.append(G[temp][i])
    return path
'''
      
def DFS(G, s, t):

    visited = [False] * len(G)
    path = [(-1, -1)] * len(G)
    stack = deque()

    visited[s] = True
    stack.append(s)

    while len(stack) > 0:

        temp = stack.pop()

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:

                path[G[temp][i]] = (temp, i)

                if G[temp][i] == t:
                    return path
                
                visited[G[temp][i]] = True

                stack.append(G[temp][i])

    return path

def binworker( M ):
    #print(M)

    G = [ [] for _ in range((len(M) * 2) + 2)]

    for i in range(len(M)):
        for j in range(len(M[i])):
            G[M[i][j]].append(i + len(M))

    for i in range(len(M)):
        G[len(G) - 2].append(i)
        G[i+len(M)].append(len(G) - 1)
    
    #for i in range(len(G)):
    #    print(G[i])

    s = len(G) - 2
    t = len(G) - 1

    flow = 0

    path = DFS(G, s, t)

    x = t
    while path[x][0] != -1:

        G[path[x][0]].pop(path[x][1])
        G[x].append(path[x][0])

        x = path[x][0]
        
    res = path[t][0]

    #print("\n", end='')
    while(res != -1):

        flow+=1

        path = DFS(G, s, t)

        x = t
        while path[x][0] != -1:

            G[path[x][0]].pop(path[x][1])
            G[x].append(path[x][0])

            x = path[x][0]
        
        res = path[t][0]
    
    return flow


    '''M = [ [ 0, 1, 3], #5
    [ 2, 4], #6
    [ 0, 2], #7
    [ 3 ], #8
    [ 3, 2] ] #9
    '''
#M = [[0, 1], [0, 1], [0]]

#print(binworker(M))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )
