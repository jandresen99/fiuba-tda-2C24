from pulp import LpProblem, LpVariable, LpMinimize

# Creamos el problema
problema = LpProblem("Minimización", LpMinimize)

# Definimos las variables de decisión, con lowBound indicamos que tienen que ser positivas
x1 = LpVariable("x1", lowBound=0)  # x1 >= 0
x2 = LpVariable("x2", lowBound=0)  # x2 >= 0
x3 = LpVariable("x3", lowBound=0)  # x3 >= 0
x4 = LpVariable("x4", lowBound=0)  # x4 >= 0
x5 = LpVariable("x5", lowBound=0)  # x5 >= 0
x6 = LpVariable("x6", lowBound=0)  # x6 >= 0

# Definimos la función objetivo
problema += x1 + x2 + x3 + x4 + x5 + x6, "Función Objetivo"

# Indicamos las restricciones
problema += x1 + x6 >= 15, "Restricción 1"
problema += x1 + x2 >= 35, "Restricción 2"
problema += x2 + x3 >= 65, "Restricción 3"
problema += x3 + x4 >= 80, "Restricción 4"
problema += x4 + x5 >= 40, "Restricción 5"
problema += x5 + x6 >= 25, "Restricción 6"

problema.solve()

# Resultados
print("Valor óptimo de Z:", problema.objective.value())
print("Valor óptimo de x1:", x1.value())
print("Valor óptimo de x2:", x2.value())
print("Valor óptimo de x3:", x3.value())
print("Valor óptimo de x4:", x4.value())
print("Valor óptimo de x5:", x5.value())
print("Valor óptimo de x6:", x6.value())