            T[0][i] = 0

            res = x + suckOil(T, 0, i)

            A.append( (res, i) )

    print(A)
    
    pos = 0
    stopy = 0

    pq = PriorityQueue()