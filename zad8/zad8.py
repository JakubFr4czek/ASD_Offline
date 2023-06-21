from zad8testy import runtests
from queue import PriorityQueue
from collections import deque

#Jakub Fraczek
#O( (ilosc plam) )
#O(m) 

#Algorytm zachlanny
#Biore najpierw pole z najwieksza zawartroscia ropy, ktore jest w zasiegu

#Wlasnie rozumialem, ze skoro tak, czy tak zatankuje z danej plamy,
#to lepiej to zrobic wczesniej, czyli to drugie i kolejne wystapienie
#tej samej plamy mnie nie interesuje

def suckOil(T, i, j):

    ropa = 0   
    if i - 1 >= 0 and T[i - 1][j] != 0:

            ropa += T[i - 1][j]
            T[i - 1][j] = 0
            ropa += suckOil(T, i - 1, j)

    if i + 1 < len(T) and T[i + 1][j] != 0:

            ropa += T[i + 1][j]
            T[i + 1][j] = 0
            ropa += suckOil(T, i + 1, j)

    if j - 1 >= 0 and T[i][j - 1] != 0:

            ropa += T[i][j - 1]
            T[i][j - 1] = 0
            ropa += suckOil(T, i, j - 1)

    if j + 1 < len(T[i]) and T[i][j + 1] != 0:

            ropa += T[i][j + 1]
            T[i][j + 1] = 0
            ropa += suckOil(T, i, j + 1)

    return ropa

def plan(T):
    
    #if len(T[0]) == 5:
    #    for i in range(len(T)):
    #        print(T[i])

    A = deque()

    for i in range(len(T[0])):

        if T[0][i] != 0:
            x = T[0][i]
            T[0][i] = 0

            res = x + suckOil(T, 0, i)

            A.append( (-1 * res, i) ) # -1 bo priorityqueue jest minheapem

    #print(A)
    
    pos = 0
    stopy = 0

    pq = PriorityQueue()
    pq.put(A[0])
    A.popleft()

    while pos < len(T[0]) - 1 and not pq.empty():
        
        stopy+=1

        oil, stainPos = pq.get()
        
        oil *= -1 #bo priorityqueue jest minheapem

        #biere te plame ktora jest blizej

        pos += oil
        while len(A) > 0 and A[0][1] <= pos:
            pq.put(A[0])
            A.popleft()
            i+=1
       
    if pos < len(T[0]) - 1:
          return None

    return stopy


        
                
#poprawny wynik 2

T = [[2, 0, 2, 0, 5],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

#print(plan( T ))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

