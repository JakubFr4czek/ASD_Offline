from zad8testy import runtests



def path(i, oil, stops, N, R):

    #print(i, oil, stops)
    print(R)

    if oil < 0: return float('inf')

    if i < len(N) - 1:

        #print(N[i], R[N[i]])
        if N[i] != -1 and R[N[i]] != 0:

            sucked = R[N[i]]

            NOWA = [R[i] for i in range(len(R))]
            NOWA[N[i]] = 0
            #print(NOWA)
            return min(path(i + 1, oil - 1 + sucked, stops + 1, N, NOWA), path(i + 1, oil - 1, stops, N, R))
        else:
             return path(i + 1, oil - 1, stops, N, R)
        
    else:
        return stops
    
def suckOil(T, i, j, dump):

    if i == 0:
        dump.append(j)

    ropa = 0   
    if i - 1 >= 0 and T[i - 1][j] != 0:

            ropa += T[i - 1][j]
            T[i - 1][j] = 0
            ropa += suckOil(T, i - 1, j, dump)

    if i + 1 < len(T) and T[i + 1][j] != 0:

            ropa += T[i + 1][j]
            T[i + 1][j] = 0
            ropa += suckOil(T, i + 1, j, dump)

    if j - 1 >= 0 and T[i][j - 1] != 0:

            ropa += T[i][j - 1]
            T[i][j - 1] = 0
            ropa += suckOil(T, i, j - 1, dump)

    if j + 1 < len(T[i]) and T[i][j + 1] != 0:

            ropa += T[i][j + 1]
            T[i][j + 1] = 0
            ropa += suckOil(T, i, j + 1, dump)

    return ropa


def plan(T):
    
    #if len(T[0]) == 16:
    #    for i in range(len(T)):
    #        print(T[i])

    R = [] #ile ropy w danej plamie
    N = [-1] * len(T[0]) #odnosciki do plam, przez te glupie testy, gdzie plamy sie lacza

    for i in range(len(T[0])):

        if T[0][i] != 0:
            dump = []
            x = T[0][i]
            T[0][i] = 0

            R.append(x + suckOil(T, 0, i, dump))

            for i in range(len(dump)):
                N[dump[i]] = len(R) - 1

    #print(N)
    #print(R)
    res = path(0, 0, 0, N, R)
    #print(res)
    #print(x)
    #x = frog( T[0] )

    if res == float('inf'):
         return None
    return res 


T = [[3, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

T1 = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
[0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

plan( T )

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

