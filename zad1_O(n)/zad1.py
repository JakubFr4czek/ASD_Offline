from zad1testy import runtests

'''

    Jest to implementacja algorytmu Manachera, którego zrozumienie zajęło
    mi zdecydowanie więcej czasu niż powinno. Algorytm wykorzystuje palindromy
    znajdujące się wewnątrz palindromów, korzysta z tablicy pomocniczej zapisując
    tam długości znalezionych palindromów. Przemieszcza się po napisie od lewej
    do prawej oblicza długości palindromów algorytmem o(n^2) i zapisuje do tabeli.
    W trakcie, jeśli to możliwe, korzysta z wczesniej zapisanych danych. Przykładowo
    policzył, że długość palindromu o środku w punkicie x to 11, dla znaku na pozycji x+2, 
    sprawdzam czy jest równy znakowi na pozycji x-2 (odczytuje tez z tablicy długośc palindromu
    o środku x - 2), jeżeli tak, to mam pewność, że długość palindromu o środku x+2
    jest >= min(długość palindromu o środku x-2, odległośc x+5 - (x+2)).
    Jest tak ponieważ mam pewność, że palindromy są tej samej długości jedynie
    w obrębie większego palindromu, powieważ wcześniej było to sprawdzane  dla palindormu
    o środku x. Złożoność algorytmu to O(n).

'''

def ceasar( s ):
    #manacher

    N = len(s)

    maks = 0

    mid = 0
    mirr = 0
    r = 0

    tab = [0 for _ in range(N)]

    for i in range(1,N):

        ile = 0
        mirr = mid - (i-mid)

        if i < r and mirr >= 0 and s[mirr] == s[i]:
            tab[i] = min(r-i,tab[mirr])
            ile = min(r-i,tab[mirr])

        x,y = i - (1 + ile) , i + 1 + ile

        while x >= 0 and y < N and s[x] == s[y]:
            ile+=1
            x-=1
            y+=1

        tab[i] = ile
        if ile > maks:
            maks = ile

        if i + ile > r:

            mid = i
            r = mid + ile

    #print(tab)
    return (maks * 2) + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
