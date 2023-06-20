"""
Implementação do método de jacobi para solução de sistemas lineares
"""

import numpy as np

#Função do método de Jacobi
def jacobi(A, b, x0, max_iterations=100, tolerance=1e-6):
    n = len(A)
    x = np.array(x0)
    x_new = np.zeros_like(x)

    for _ in range(max_iterations):
        for p in range(n):
            sum_term = 0
            for q in range(n):
                if q != p:
                    sum_term += A[p][q] * x[q]
            x_new[p] = (b[p] - sum_term) / A[p][p]
        if np.linalg.norm(x - x_new) < tolerance:
            break

        x = np.array(x_new)

    return x

#Funçao para captura de input para solução
def get_matrix_from_input(n):
    matrix = np.zeros((n, n))
    print("Insira os elementos da matriz: ")

    for i in range(n):
        for j in range(n):
            matrix[i][j] = float(input(f"Insira valor na posiçao({i+1},{j+1}): "))

    return matrix

int_n = int(input("insira o grau da matriz: "))
print(int_n)

'''
A = np.array([[4, 1, -1],
              [3, 5, 1],
              [2, -1, 3]])
'''
A = get_matrix_from_input(int_n)
print(A)

#b = np.array([5, 7, 3])

b = np.zeros(int_n, dtype=int)
for p in range(int_n):
    b[p] = int(input(f"digite um valor para b na posiçao {p}: "))

print(b)
x0 = np.zeros_like(b)

solution = jacobi(A, b, x0)

print("Solution:", solution)
