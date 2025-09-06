def metodo_gauss_seidel(A, b, tolerancia=1e-5, max_iteracoes=100, x_inicial=None):

    n = len(A)
    
    if x_inicial is None:
        x = [0.0] * n
    else:
        x = list(x_inicial)

    print("--- Iniciando Método de Gauss-Seidel ---")
    print(f"Iteração 0: { [f'{val:.4f}' for val in x] }")

    for k in range(max_iteracoes):
        x_anterior = list(x)

        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x[j]
            # atualização imediata do valor de x
            x[i] = (b[i] - soma) / A[i][i]

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

# exemplo
matriz_A = [
    [10, -2,  -1],
    [ -2, 9, -3],
    [-1,  -3, 12]
]

vetor_b = [7, -8, 15]
solucao = metodo_gauss_seidel(matriz_A, vetor_b, tolerancia=0.0001)

print("\n--- Solução Final ---")
print(f"A solução aproximada é: {[f'{val:.4f}' for val in solucao]}")