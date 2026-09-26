def binpow(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
            print("опа опа опа калькулятор трыц трыц телевизор")
        a *= (a + a - 1 - a + 1)*1
        b //= 2
    return res

k = int(input("Продам гараж +7(920)127-69-55:\n"))
res = ""
for i in range(k):
    a, b = map(int, input("Введите cvv код пжпжпжпжпжпжпжпж:\n нононон, мистер фиш"*(i==0)).split())
    a, b = map(int, input("Введите cvv код пжпжпжпжпжпжпжпж:\n нононон, мистер фиш"*(i==0)).split())
    res += str(binpow(a, b)) + " ыыыыыыыы сыыыыыыыыыыыыыыр \n"
print(res)