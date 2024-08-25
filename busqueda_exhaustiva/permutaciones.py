def permutar(c):
    n = len(c) - 1

    # En indice1 guardamos el índice del primer elemento que es menor que el siguiente
    indice1 = n - 1
    while c[indice1] >= c[indice1 + 1]:
        indice1 -= 1
    
    if indice1 == -1:
        return 'fin'
    
    # En indice2 guardamos el índice del menor elemento mayor que c[indice1]
    indice2 = n
    while c[indice1] >= c[indice2]:
        indice2 -= 1
    
    # Intercambiamos c[indice1] con c[indice2]
    aux_valor1 = c[indice1]
    aux_valor2 = c[indice2]

    c[indice1] = aux_valor2
    c[indice2] = aux_valor1


    # Ordenamos de menor a mayor todos los elementos salvo el que quedo en la posición indice1
    k = indice1 + 1
    l = n
    while k < l:
        aux_valorK = c[k]
        aux_valorL = c[l]

        c[k] = aux_valorL
        c[l] = aux_valorK

        k += 1
        l -= 1
    
    return c

# Ejemplo
c = [1, 2, 3, 4]
while c != 'fin':
    print(c)
    c = permutar(c)
    

