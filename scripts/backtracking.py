def es_solucion(estado_actual):
    # Completar con la condicion de solucion
    return True

def supera_propiedad_corte(estado_actual):
    # Completar con la propiedad de corte
    return True

def sucesores(estado_actual):
    # Completar con el calculo de los sucesores
    return []

def backtrack(estado_actual):
    if es_solucion(estado_actual):
        return estado_actual
    
    if supera_propiedad_corte(estado_actual):
        for posible_sucesor in sucesores(estado_actual):
            resultado = backtrack(posible_sucesor)

            if es_solucion(resultado):
                return resultado
    
    return None