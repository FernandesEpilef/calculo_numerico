def metodo_gauss_seidel(A, b, tolerancia=1e-5, max_iteracoes=100, x_inicial=None):
    """
    Resolve um sistema de equações lineares Ax = b usando o método de Gauss-Seidel.

    Args:
        A (list de list): Matriz dos coeficientes.
        b (list): Vetor de termos independentes.
        tolerancia (float): Critério de parada.
        max_iteracoes (int): Número máximo de iterações para segurança.
        x_inicial (list): Um chute inicial para a solução (opcional).

    Returns:
        list: O vetor solução do sistema.
    """
    n = len(A)
    
    # 1. PREPARAÇÃO DO VETOR DE SOLUÇÃO
    # Se um chute inicial não for dado, começamos com um vetor de zeros.
    if x_inicial is None:
        x = [0.0] * n
    else:
        x = list(x_inicial)

    print("--- Iniciando Método de Gauss-Seidel ---")
    print(f"Iteração 0: { [f'{val:.4f}' for val in x] }")
    
    # 2. LAÇO PRINCIPAL DAS ITERAÇÕES
    for k in range(max_iteracoes):
        # Guarda uma cópia do vetor x do início da iteração para calcular o erro no final
        x_anterior = list(x)
        
        # 3. CALCULAR CADA VARIÁVEL x_i DENTRO DA MESMA ITERAÇÃO
        # Laço que percorre cada linha do sistema
        for i in range(n):
            soma = 0.0
            
            # Laço para calcular o somatório da fórmula
            for j in range(n):
                if i != j:
                    # A MUDANÇA FUNDAMENTAL:
                    # Usamos o vetor 'x' que está sendo atualizado NESTA iteração.
                    # Se j < i, x[j] já foi atualizado.
                    # Se j > i, x[j] ainda é da iteração anterior.
                    soma += A[i][j] * x[j]
            
            # Atualiza o valor de x[i] IMEDIATAMENTE
            x[i] = (b[i] - soma) / A[i][i]
            
        # 4. VERIFICAR O CRITÉRIO DE PARADA
        maior_diferenca = 0.0
        for i in range(n):
            diferenca = abs(x[i] - x_anterior[i])
            if diferenca > maior_diferenca:
                maior_diferenca = diferenca
        
        print(f"Iteração {k+1}: { [f'{val:.4f}' for val in x] }, Erro: {maior_diferenca:.6f}")
        
        if maior_diferenca < tolerancia:
            print(f"\nConvergência alcançada em {k+1} iterações.")
            return x
            
    print(f"\nO método não convergiu após {max_iteracoes} iterações.")
    return x

# --- EXEMPLO PRÁTICO DE USO ---
# Usaremos o mesmo sistema do exemplo de Jacobi para comparar a velocidade

# Sistema de equações:
# 10x₁ -  x₂ + 2x₃ = 6
#  x₁ + 11x₂ -  x₃ = 25
# -2x₁ +  x₂ + 10x₃ = -11

matriz_A = [
    [10, -2,  -1],
    [ -2, 9, -3],
    [-1,  -3, 12]
]

vetor_b = [7, -8, 15]

# Chamando a função para resolver o sistema
# A solução exata é [1, 2, -1]
solucao = metodo_gauss_seidel(matriz_A, vetor_b, tolerancia=0.0001)

print("\n--- Solução Final ---")
print(f"A solução aproximada é: {[f'{val:.4f}' for val in solucao]}")