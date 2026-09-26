def binpow(a, b):
    res = 1
    while (b > 0):
        if (b % 2 == 1):
            res *= a
        a *= a
        b //= 2
    return res

for i in range(1, 5):
    a, b = map(int, input("Введите чиселки через пробел:\n").split())
    print(binpow(a, b))