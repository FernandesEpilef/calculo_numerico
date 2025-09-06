import numpy as np

def simpson(f, a, b, n):
    if n % 2 != 0:
        print("Erro: O número de subintervalos (n) deve ser par.")
        return None

    h = (b - a) / n
    soma = f(a) + f(b)

    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)

    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)

    return (h / 3) * soma

#exemplo
def exemplo(x):
    return np.exp(-x**2)

limite_inferior = 0
limite_superior = 3
n = 9
num_intervalos = n -1

resultado = simpson(exemplo, limite_inferior, limite_superior, num_intervalos)

print(f"Função: f(x) = x³")
print(f"Intervalo: [{limite_inferior}, {limite_superior}], n = {num_intervalos}")
print("-" * 35)

if resultado is not None:
    print(f"Valor aproximado da integral: {resultado:.6f}")