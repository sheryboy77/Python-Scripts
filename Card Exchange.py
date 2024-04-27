def Frequencies(arr):
    n = len(arr)
    mp = dict()

    # Traverse through array elements
    # and count frequencies
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    kp = list(mp.items())
    return kp
    # Traverse through map and print
    # frequencies
    #for x in mp:
    #    card_freq = (x, mp[x])
    #    return card_freq


def solve():
    n,k = 5,3 #input("line1: ").split()
    cards = [4, 1, 1, 4, 4]#input("line2: ").split()

    card_freq = (Frequencies(cards))
    print(card_freq[1][1])


solve()

