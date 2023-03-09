from zad1testy import runtests 

'''

    Sprawdzam czy substring jest palindromem zaczynając sprawdzanie od
    jego środka do zewnątrz. Gdy natknę się na najmniejszy palindrom czyli
    przykładowo aba to sprawdzam czy znak przed aba jest równy znakowi po aba
    i tak dalej, a jeżeli są różne to kończe sprawdzanie i zapisuję długość
    palindromu. Mam wrażenie, że to około O(n^2).

'''

def ceasar( s ):

    N = len(s)

    maks = 1

    for i in range(N-2):

        if s[i] == s[i + 2]:

            ile = 3

            x,y = i - 1, i + 3

            while x >= 0 and y < N and s[x] == s[y]:
                ile+=2
                x-=1
                y+=1
            if ile > maks:
                maks = ile
    return maks



#print(ceasar("akontnoknonabcddcba"))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
