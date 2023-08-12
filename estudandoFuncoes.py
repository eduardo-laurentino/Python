def maximo(a, b):
    if a > b:
        return a
    else:
        return b

def multiplo(a, b):
    return a % b == 0    


def area_quadrado(l):
    return l ** 2


def area_triangulo(b, h):
    return (b * h) / 2


def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

def soma(l):
    total = 0
    for e in l:
        total += e
    return total


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return abs(a*b) / mdc(a, b)

def valida_string(s, mín, máx):
    tamanho = len(s)
    return mín <= tamanho <= máx


def procura_string(s, lista):
    return s in lista


print(f"máximo(5,6) == 6 -> obtido: {maximo(5,6)}")
print(f"máximo(2,1) == 2 -> obtido: {maximo(2,1)}")
print(f"máximo(7,7) == 7 -> obtido: {maximo(7,7)}")


print(f"múltiplo(8,4) == True -> obtido: {multiplo(8,4)}")
print(f"múltiplo(7,3) == False -> obtido: {multiplo(7,3)}")
print(f"múltiplo(5,5) == True -> obtido: {multiplo(5,5)}")


print(f"área_quadrado(4) == 16 -> obtido: {area_quadrado(4)}")
print(f"área_quadrado(9) == 81 -> obtido: {area_quadrado(9)}")


print(f"área_triângulo(6, 9) == 27 -> obtido: {area_triangulo(6,9)}")
print(f"área_triângulo(5, 8) == 20 -> obtido: {area_triangulo(5,8)}")


l = [10, 20, 25, 30]
print(pesquise(l, 25))
print(pesquise(l, 27))


l = [1, 7, 2, 9, 15]
print(soma(l))
print(soma([7, 9, 12, 3, 100, 20, 4]))


print(f"MDC 10 e 5 --> {mdc(10,5)}")
print(f"MDC 32 e 24 --> {mdc(32,24)}")
print(f"MDC 5 e 3 --> {mdc(5,3)}")


print(f"MMC 10 e 5 --> {mmc(10, 5)}")
print(f"MMC 32 e 24 --> {mmc(32, 24)}")
print(f"MMC 5 e 3 --> {mmc(5, 3)}")


print(valida_string("", 1, 5))
print(valida_string("ABC", 2, 5))
print(valida_string("ABCEFG", 3, 5))
print(valida_string("ABCEFG", 1, 10))


l = ["AB", "CD", "EF", "FG"]
print(procura_string("AB", l))
print(procura_string("CD", l))
print(procura_string("EF", l))
print(procura_string("FG", l))
print(procura_string("XYZ", l))