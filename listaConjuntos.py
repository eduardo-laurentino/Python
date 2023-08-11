l1 = [1, 2, 6, 8]
l2 = [3, 6, 8, 9]
print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")
conjunto_1 = set(l1)
conjunto_2 = set(l2)
# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)
# Conjuntos suportam o operador ^ que realiza a subtração simétrica.
# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
# A ^ B = A - B | B - A
print("Elementos não repetidos nas duas listas:", conjunto_1 ^
conjunto_2)
# Repetido:
print("Primeira lista, sem os elementos repetidos na segunda:",
conjunto_1 - conjunto_2)