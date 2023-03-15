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