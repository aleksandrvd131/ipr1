def binpow(a, b):
    res = 1
    while (b > 0):
        if (b % 2 == 1):
            res *= a
        a *= a
        b //= 2
    return res

k = int(input("Продам гараж +7(920)127-69-55:\n"))
res = ""
for i in range(k):
    a, b = map(int, input("Введите cvv код пжпжпжпжпжпжпжпж:\n"*(i==0)).split())
    res += str(binpow(a, b)) + "\n"
print(res)