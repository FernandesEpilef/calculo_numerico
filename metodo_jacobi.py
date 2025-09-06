def metodo_jacobi(A, b, tolerancia=1e-5, max_iteracoes=100, x_inicial=None):
    n = len(A)

    if x_inicial is None:
        x = [0.0] * n
    else:
        x = list(x_inicial)
    x_novo = [0.0] * n
    
    print("--- Iniciando Método de Jacobi ---")
    print(f"Iteração 0: { [f'{val:.4f}' for val in x] }")

    for k in range(max_iteracoes):
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x[j]
            x_novo[i] = (b[i] - soma) / A[i][i]
        maior_diferenca = 0.0
        for i in range(n):
            diferenca = abs(x_novo[i] - x[i])
            if diferenca > maior_diferenca:
                maior_diferenca = diferenca
        
        x = list(x_novo)

        print(f"Iteração {k+1}: { [f'{val:.4f}' for val in x] }, Erro: {maior_diferenca:.6f}")

        if maior_diferenca < tolerancia:
            print(f"\nConvergência alcançada em {k+1} iterações.")
            return x
            
    # Se o laço terminar sem convergência
    print(f"\nO método não convergiu após {max_iteracoes} iterações.")
    return x

#exemplo
matriz_A = [
    [12, 3,  2],
    [ -3, 10, -1],
    [2,  -1, 8]
]

vetor_b = [15, 27, -9]

solucao = metodo_jacobi(matriz_A, vetor_b, tolerancia=0.0001)

print("\n--- Solução Final ---")
print(f"A solução aproximada é: {[f'{val:.4f}' for val in solucao]}")