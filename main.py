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
    print("Enter the elements of the matrix:")

    for i in range(n):
        for j in range(n):
            matrix[i][j] = float(input(f"Enter element at position ({i+1},{j+1}): "))

    return matrix



int_n = int(input("insira o grau da matriz: "))

'''
A = np.array([[4, 1, -1],
              [3, 5, 1],
              [2, -1, 3]])
'''
A = get_matrix_from_input(int_n)

b = np.array([5, 7, 3])

x0 = np.zeros_like(b)

solution = jacobi(A, b, x0,)

print("Solution:", solution)
