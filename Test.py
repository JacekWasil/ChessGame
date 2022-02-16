krotka1 = (1, 2, 3)
krotka2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def czysiezawieraXwY(x, y):
    out = True
    xlen = len(x)
    w = 0
    while w < xlen :
        if x[w] not in y :
            out = False
        w = w + 1
    return out

print ('dupaa')


print(czysiezawieraXwY(krotka1, krotka2))