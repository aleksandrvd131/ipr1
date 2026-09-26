def binpow(a, b):
    res = 1
    while (a > 0):
        if (a % 2 == 1):
            res *= a
        a *= a
    return res

binpow(3,4) #33902193-2103i9-21