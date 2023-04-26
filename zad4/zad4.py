from zad4testy import runtests
from collections import deque

def bfs(G, poczatek, koniec, banned1, banned2):

    visited = [False for _ in range(len(G))]

    queue = deque()
    skad = [ -1 for _ in range(len(G))]

    queue.append(poczatek)
    visited[poczatek] = True

    while len(queue) > 0:
         
        temp = queue.popleft()
        if temp == koniec:
            break

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:

                if (temp != banned1 or G[temp][i] != banned2) and (temp != banned2 or G[temp][i] != banned1):
                    queue.append(G[temp][i])
                    skad[G[temp][i]] = temp
                    visited[G[temp][i]] = True
                    

    if skad[koniec] == -1:
        return []

    res = deque()

    pos = koniec

    while pos != poczatek:

        res.append(pos)

        pos = skad[pos]
    res.append(poczatek)
    #print(res)
    return res

    #if len(sciezka) %2 == 1:
    #    return (len(sciezka)//2) - 1
    #return len(sciezka)//2


def longer(G, poczatek, koniec):

    sciezka = deque()

    sciezka = bfs(G, poczatek, koniec ,-1 ,-1) #najkrotsza sciezka (tak mi sie wydaje)


    #print(sciezka)

    if len(sciezka) == 0:
        return None

    #print(sciezka)

    res = bfs(G, poczatek, koniec, sciezka[0], sciezka[1])
    
    res2 = (sciezka[0], sciezka[1])

    for i in range(2, len(sciezka)):

        temp = bfs(G, poczatek, koniec, sciezka[i - 1], sciezka[i])
        #print(sciezka[i - 1], sciezka[i])
        if len(temp) == 0: return (sciezka[i - 1], sciezka[i])
        if len(temp) > len(res):
            res = temp
            res2 = (sciezka[i - 1], sciezka[i])

    if len(res) > len(sciezka):
        return res2
    elif len(res) == 0:
        return res2
    else:
        return None
    


#G = [[4, 6], [2,6], [1, 3], [2, 5], [0, 5], [4, 3], [0,1]]

#print(longer(G, 0, 2))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )