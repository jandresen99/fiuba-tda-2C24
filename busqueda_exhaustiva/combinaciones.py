def incrementar(c, m):
    j = 0

    while c[j]+1 == c[j+1]:
        c[j] = j + 1
        j += 1
    
    if j+1 > m:
        return 'fin'
    
    c[j] += 1
    return c

# Ejemplo
c = [0, 8, 4, 3, 2, 1]
print(c)
caux = c[::-1]
while caux != 'fin':
    caux = incrementar(caux, 4)
    print(caux[::-1])