def incrementar(c):
    n = len(c)

    pos = n - 1

    # Desde la derecha, cambiamos todos los 1 por 0 hasta encontrar un 0
    while c[pos] == 1 and pos >= 0:
        c[pos] = 0
        pos -= 1

    # Si no encontramos un 0, terminamos
    if pos == -1:
        return 'fin'
    
    # Si encontramos un 0, lo cambiamos por 1
    c[pos] = 1
    return c

# Ejemplo
c = [0, 0, 0]
while c != 'fin':
    print(c)
    c = incrementar(c)