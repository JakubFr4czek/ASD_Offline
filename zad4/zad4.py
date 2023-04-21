from zad4testy import runtests
from collections import deque

def bfs(G, poczatek, koniec, banned1, banned2):

    visited = [False for _ in range(len(G))]

    queue = deque()
    sciezka = deque()
    skad = [ -1 for _ in range(len(G))]

    queue.append(poczatek)
    visited[poczatek] = True

    while len(queue) > 0:
         
        temp = queue.popleft()
        sciezka.append(temp)
        if temp == koniec:
            break

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:

                if (temp != banned1 or G[temp][i] != banned2) and (temp != banned2 or G[temp][i] != banned1):
                    queue.append(G[temp][i])
                    skad[G[temp][i]] = temp
                    visited[G[temp][i]] = True

    print("skad: ",skad)

    if sciezka[len(sciezka) - 1] != koniec: #sciezki nie znaleziono
        return []

    #ekstrakcja sciezki (fajnie brzmi)

    res = deque()

    if len(sciezka) %2 == 1:
        res.append(sciezka[0])
        #print(len(sciezka)//2)
        for i in range(2, len(sciezka), 2):
            res.append(sciezka[i])
    else:
        res.append(sciezka[0])
        for i in range(1, len(sciezka), 2):
            res.append(sciezka[i])
    
    return res

    #if len(sciezka) %2 == 1:
    #    return (len(sciezka)//2) - 1
    #return len(sciezka)//2


def longer(G, poczatek, koniec):

    sciezka = deque()

    sciezka = bfs(G, poczatek, koniec ,-1 ,-1) #najkrotsza sciezka (tak mi sie wydaje)
    if len(sciezka) == 0:
        return 0

    #print(sciezka)

    res = bfs(G, poczatek, koniec, sciezka[0], sciezka[1])
    print(res)
    res2 = (sciezka[0], sciezka[1])

    for i in range(2, len(sciezka)):

        temp = bfs(G, poczatek, koniec, sciezka[i - 1], sciezka[i])

        if len(temp) < len(res):
            res = temp
            res2 = (sciezka[i - 1], sciezka[i])

    if len(temp) > len(sciezka):
        return res2
    else:
        return 0
    


G = [[4, 6], [2,6], [1, 3], [2, 5], [0, 5], [4, 3], [0,1]]

print(longer(G, 0, 2))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( longer, all_tests = False )