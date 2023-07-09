from zad7testy import runtests

#Jakub Fraczek
#O(n^2)

# Algorytm najpierw liczy ile mozna zyskac idac w dol, 
# nastepnie idzie od dolu do gory i liczy max z tych wartosci dla danego pola.
# Poprostu szukam maksymalej wartosci jaka moge osiagnac dla dadanego pola i tak dalej
# dla kolejnych, az dojde to tego ostatniego, szukanego.

def maze( L ):

    dp = [[ 0 for j in range(len(L)) ] for i in range(len(L))]

    #NxN
    for i in range(len(L)):

        #Pierwsza petla idzie w dol
        for j in range(len(L)):


            if L[j][i] == '#':
                dp[j][i] = float('-inf')

                #Jak sie natkne na inf na 0-rowej kolumnie to juz nizej nie mozna isc
                if i == 0:
                    for k in range(j, len(L)):
                        dp[k][i] = float('-inf')
                    break

                continue
            
            #To sa wartosci defaultowe, poza tablica, no sila rzeczy poza tablica nic nie ma, czyli -inf
            lewy, gorny = float('-inf'), float('-inf')

            #Sila rzeczy tu musi byc 0, bo gdzies trzeba zaczac
            if i == 0:
                lewy = 0
                gorny = 0

            #Tutaj wyliczam czy bardziej sie oplacalo przyjsc do tego pola z lewej strony, czy od gory
            #i w obu przypadkach:
            # - jak przyszedlem od gory to zwiekszam o 1
            # - jak przyszedlem od lewej to tez zwiekszam o 1
            # Moze i ta jedynka w lini 52 nie oznacza zawsze tego samego, ale sie redukuje do tego samego

            if i - 1 >= 0:
                lewy = dp[j][i - 1]
            if j - 1 >= 0:
                gorny = dp[j - 1][i]

            dp[j][i] = max(lewy, gorny) + 1
        
        #Druga petla idzie w gore


        #W pierwszej iteracji nie da sie isc w gore, bo startujemy z lewego gornego
        if i == 0: continue 

        dolny = float('-inf')

        for j in range(len(L) -1, -1, -1):

            if L[j][i] == '#':
                dp[j][i] = float('-inf')
                dolny = float('-inf')
                continue

            lewy = float('-inf')

            if i - 1 >= 0:
                lewy = dp[j][i - 1]
            
            dp[j][i] = max(dp[j][i], max(lewy, dolny) + 1)

            #Tutaj zachowouje wartosc, bo jest opcja, ze dp[j][i] jest najwieksza wartoscia,
            #a jest to wartosc osiagnieta idac w dol po danej kolumnie i nie moge jej teraz
            #uzyc idac w gore, bo to by bylo tak jak bym dwa razy sie przeszedl po tej kolumnie
            #Wiec zachowuje ta wartosc osiagnieta idac od dolu i probuje czy idac od dolu
            #moge osiagnac jakas wieksza wartosc dla wyzszego pola, jesli tak to poprostu podmieniam
            #i to nie przeszkadza w tym ze jedne wartosci beda pochodzic z przejsca od gory, a drugie 
            #od dolu, bo to poptostu jest maksymalna wartosc jaka mozna osiagnac dla danego pola
            dolny = max(lewy, dolny) + 1
    
    if dp[len(L) - 1][len(L) - 1] == float('-inf'):
        return -1
    return dp[len(L) - 1][len(L) - 1] - 1

    
             
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )


