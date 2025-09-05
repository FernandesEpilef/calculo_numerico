import math # Usaremos para verificar se algum número é inválido

def metodo_jacobi(A, b, tolerancia=1e-5, max_iteracoes=100, x_inicial=None):
    n = len(A) # Tamanho do sistema
    
    # 1. PREPARAÇÃO DOS VETORES DE SOLUÇÃO
    # Se um chute inicial não for dado, começamos com um vetor de zeros.
    if x_inicial is None:
        x = [0.0] * n
    else:
        x = list(x_inicial)

    # Vetor para armazenar a solução da PRÓXIMA iteração
    x_novo = [0.0] * n
    
    print("--- Iniciando Método de Jacobi ---")
    print(f"Iteração 0: { [f'{val:.4f}' for val in x] }")
    
    # 2. LAÇO PRINCIPAL DAS ITERAÇÕES
    for k in range(max_iteracoes):
        
        # 3. CALCULAR CADA VARIÁVEL x_i DA PRÓXIMA ITERAÇÃO
        for i in range(n):
            soma = 0.0
            
            # Laço para calcular o somatório da fórmula de Jacobi
            for j in range(n):
                # A condição fundamental: somamos apenas quando j é diferente de i
                if i != j:
                    soma += A[i][j] * x[j] # Usa os valores da iteração ANTERIOR (vetor x)
            
            # Aplica a fórmula completa para encontrar o novo valor de x_i
            x_novo[i] = (b[i] - soma) / A[i][i]
        
        # 4. VERIFICAR O CRITÉRIO DE PARADA
        maior_diferenca = 0.0
        for i in range(n):
            diferenca = abs(x_novo[i] - x[i])
            if diferenca > maior_diferenca:
                maior_diferenca = diferenca
        
        # Atualiza o vetor de solução para a próxima iteração
        x = list(x_novo)

        print(f"Iteração {k+1}: { [f'{val:.4f}' for val in x] }, Erro: {maior_diferenca:.6f}")

        # Se a maior diferença for menor que nossa tolerância, a solução convergiu!
        if maior_diferenca < tolerancia:
            print(f"\nConvergência alcançada em {k+1} iterações.")
            return x
            
    # Se o laço terminar sem convergência, avisamos o usuário
    print(f"\nO método não convergiu após {max_iteracoes} iterações.")
    return x

matriz_A = [
    [12, 3,  2],
    [ -3, 10, -1],
    [2,  -1, 8]
]

# Vetor b
vetor_b = [15, 27, -9]

solucao = metodo_jacobi(matriz_A, vetor_b, tolerancia=0.0001)

print("\n--- Solução Final ---")
print(f"A solução aproximada é: {[f'{val:.4f}' for val in solucao]}")