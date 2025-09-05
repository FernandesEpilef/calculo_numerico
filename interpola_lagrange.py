def interpolacao_lagrange_detalhada(pontos_x, pontos_y, valor_x):

    n = len(pontos_x)
    resultado_final = 0.0

    valores_L = []

    for i in range(n):

        termo_L = 1.0
        
        for j in range(n):
            if i != j:
                numerador = valor_x - pontos_x[j]
                denominador = pontos_x[i] - pontos_x[j]
                termo_L = termo_L * (numerador / denominador)
        
        valores_L.append(termo_L)
        
        resultado_final += pontos_y[i] * termo_L
        
    return resultado_final, valores_L

# --- EXEMPLO PRÁTICO ---

x_conhecidos = [8.0, 8.5, 9.0, 10.0]
y_conhecidos = [2.0, 2.0408, 2.0801, 2.1544]

x_descoberto = 9.75

y_descoberto, lista_L = interpolacao_lagrange_detalhada(
    x_conhecidos, y_conhecidos, x_descoberto
)

# 4. Mostre os resultados!
print("--- Interpolação de Lagrange (Detalhada) ---")
print(f"Pontos X conhecidos: {x_conhecidos}")
print(f"Pontos Y conhecidos: {y_conhecidos}")
print(f"Calculando para x = {x_descoberto}")
print("-" * 35)

print("Valores dos Polinômios de Base L(x):")
for i in range(len(lista_L)):
    print(f"  L_{i}({x_descoberto}) = {lista_L[i]:.4f}")

print(f"Resultado final: y({x_descoberto}) = {y_descoberto:.4f}")