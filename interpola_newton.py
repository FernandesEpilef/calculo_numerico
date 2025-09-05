def imprimir_tabela_iniciante(tabela, pontos_x):

    print("\n--- Tabela de Diferenças Divididas ---")
    
    n = len(pontos_x)

    print("i", end='\t')
    print("x[i]", end='\t')
    print("y[i]", end='\t')
    for i in range(1, n):
        print(f"Ordem {i}", end='\t')
    print() 
    #print("-------------------------------------------------")

    for i in range(n):
        print(i, end='\t')
        print(f"{pontos_x[i]:.2f}", end='\t') # Formata x para 2 casas decimais

        for j in range(n):
            if j <= i:
                print(f"{tabela[i][j]:.4f}", end='\t')
        print()


def interpolacao_newton_com_tabela(pontos_x, pontos_y, valor_x):
    n = len(pontos_x)
    tabela = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        tabela[i][0] = pontos_y[i]

    for j in range(1, n):
        for i in range(j, n):
            numerador = tabela[i][j-1] - tabela[i-1][j-1]
            denominador = pontos_x[i] - pontos_x[i-j]
            tabela[i][j] = numerador / denominador

    coeficientes = [tabela[i][i] for i in range(n)]
    
    resultado = coeficientes[0]
    termo = 1.0
    
    for i in range(1, n):
        termo = termo * (valor_x - pontos_x[i-1])
        resultado = resultado + coeficientes[i] * termo
        
    return resultado, tabela

# --- EXEMPLO PRÁTICO ---

x_conhecidos = [0, 1, 2, 10, 11, 13]
y_conhecidos = [0.5, 3.3, 5.3, 9.9, 10.2, 9]

# 2. Defina o ponto que você quer descobrir
x_descoberto = 5

# 3. Chame a função para calcular o resultado E a tabela
y_descoberto, tabela_calculada = interpolacao_newton_com_tabela(
    x_conhecidos, y_conhecidos, x_descoberto
)

# 4. Mostre os resultados!
print("--- Interpolação de Newton (com Tabela Simples) ---")
print(f"Pontos X conhecidos: {x_conhecidos}")
print(f"Pontos Y conhecidos: {y_conhecidos}")

# Chama a nova função de impressão, mais simples de entender
imprimir_tabela_iniciante(tabela_calculada, x_conhecidos)

print("\n--- Resultado Final ---")
print(f"Para x = {x_descoberto}, o valor estimado de y é: {y_descoberto:.4f}")
