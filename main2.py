import numpy as np


def get_matrix_from_input(n):
    '''Recebe os valores a serem calculados em forma de matriz''' 
    matrix = np.zeros((n, n))
    print("Insira os elementos da matriz: ")

    for i in range(n):
        for j in range(n):
            matrix[i][j] = float(input(f"Insira valor na posiçao({i+1},{j+1}): "))

    return matrix

def get_inter_inic(n):
    '''retorna o vetor de valores para x^0'''
    x0 = np.zeros(n)
    for p in range(n):
        x0[p] = float(input(f"Insira valor na posiçao({i+1},{j+1}): "))
    return x0

grau_da_matriz = int(input("insira o grau da matriz: "))
print(f"o grau da matriz é: {grau_da_matriz}")

matriz = list(map(int, input().split()))
matriz = np.array(matriz).reshape(grau_da_matriz, grau_da_matriz) 
#get_matrix_from_input(grau_da_matriz)
print(f"A matriz do sistema a ser calculado é: {matriz}")

inter_inic = get_inter_inic(grau_da_matriz)
print(f"os valores de x0 são: {inter_inic}")

tol = int(input("Insira um valor para o expoente da tolerância:"))
tol = 10**tol
print(f"o valor da tolerância é: {tol}")

Max = int(input("Insira o valor máximo de interações"))
print(f"o valor máximo de interações é: {Max}")