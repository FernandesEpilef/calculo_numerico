import numpy as np

def trapezios_composto(f, a, b, n):
    h = (b - a) / n
    
    soma_dos_termos = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        soma_dos_termos += 2 * f(xi)
        
    integral_aproximada = (h / 2) * soma_dos_termos
    
    return integral_aproximada

def funcao(x):
    return np.exp(-x**2)

limite_inferior = 0
limite_superior = 3
num_trapezios = 9

resultado_aproximado = trapezios_composto(funcao, limite_inferior, limite_superior, num_trapezios)

print("--- Método dos Trapézios Compostos ---")
print(f"Função: f(x) = x² + 2")
print(f"Intervalo de integração: [{limite_inferior}, {limite_superior}]")
print(f"Número de trapézios (n): {num_trapezios}")
print("-" * 35)
print(f"Valor aproximado da integral: {resultado_aproximado:.6f}")
