from zad2testy import runtests

'''

    W algorytmie korzystam ze struktry max-heap w celu znalezienia 
    paru kolejnnych największych elementow w tablicy. Nie ma potrzeby
    sortowania calosci przy pomocy heapsorta. Wybieram najwieksze
    elementy dopoki (ilosc sniegu - liczba dni które upłynęły) > 0.
    Złożoność obliczeniowa O(nlogn)


'''

def heapify(tab, N, i):

    #ustawiam największy element do rodzica

    left = 2*i
    right = 2*i + 1

    maks = i

    if left < N and tab[left] > tab[maks]:
        maks = left
    
    if right < N and tab[right] > tab[maks]:
        maks = right

    if maks != i:
        tab[i], tab[maks] = tab[maks], tab[i]

        heapify(tab, N, maks)
        
    
def maxHeap(tab):

    for i in range((len(tab)//2) - 1, -1, -1):
        heapify(tab, len(tab), i) 
    #teraz mam poprawnie zbudowany kopiec





def snow( S ):
    
    maxHeap(S)
    snieg = 0

    for i in range(len(S)): #uplywajace dni

        if S[0] - i > 0:
            #print(S)
            snieg += S[0] - i

            S[0], S[len(S) - 1 - i] = S[len(S) - 1 - i], S[0] #usuwam najwieksza wartosc z kopca i biore nastepna

            heapify(S, len(S) - 1 - i, 0) #naprawiam kopiec
        else:
            break
    
    return snieg


#tab = [1,7,3,4,1]
#print(snow(tab))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
