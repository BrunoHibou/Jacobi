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
        x0[p] = float(input(f"Insira o valor de x_{p+1}): "))
    return x0

def Jacobi(matriz, b, x0, tol, max, grau):
    '''funçao que aplica o método de jacobi'''
    if(grau == 3):
        f1 = lambda x,y,z: (b[0]- matriz[0][1]*y+ matriz[0][2]*z)/matriz[0][0]
        f2 = lambda x,y,z: (b[1]-matriz[1][0]*x+matriz[1][2]*z)/matriz[1][1]
        f3 = lambda x,y,z: (b[2]-matriz[2][0]*x+matriz[2][1]*y)/matriz[2][2]
    
    if(grau == 2):
        pass
    
    # Implementation of Jacobi Iteration
    print('\nCount\tx1\tx2\tx3\n')
    
    count = 1
    condition = True
    
    x_temp=x0
    x = x_temp
    print(f'x: {x}')
    while condition:
        
        if grau == 3:
            x_temp[0] = f1(x[0], x[1], x[2])
            #print(f'temp0: {x_temp[0]}')
            x_temp[1] = f2(x[0], x[1], x[2])
            #print(f'temp1: {x_temp[1]}')
            x_temp[2] = f3(x[0], x[1], x[2])
            #print(f'temp2: {x_temp[2]}')

            #print('%d\t%0.7f\t%0.7f\t%0.7f\t%0.7f\t%0.7f\t%0.7f\n' %(count, x_temp[0],x_temp[1],x_temp[2],e1,e2,e3))
            
            e1 = abs(x[0]-x_temp[0]);
            e2 = abs(x[1]-x_temp[1]);
            e3 = abs(x[2]-x_temp[2]);
            
            print('%d\t%0.7f\t%0.7f\t%0.7f\t%f\t%f\t%f\n' %(count, x_temp[0],x_temp[1],x_temp[2],e1,e2,e3))
            count+=1
            x = x_temp

            condition = e1<tol and e2<tol and e3<tol and count<=max
    return x
    

grau_da_matriz = int(input("insira o grau da matriz: "))
print(f"o grau da matriz é: {grau_da_matriz}")

matriz = list(map(int, input('Insira os valores da matriz em ordem separado por espaço:\n').split()))
matriz = np.array(matriz).reshape(grau_da_matriz, grau_da_matriz) 
#get_matrix_from_input(grau_da_matriz)
print(f"A matriz A do sistema a ser calculado é:\n{matriz}")

b = list(map(int, input("Insira a matriz B: ").split())) 
#get_matrix_from_input(grau_da_matriz)
print(f"A matriz B do sistema a ser calculado é: {b}")

inter_inic = get_inter_inic(grau_da_matriz)
print(f"os valores de x0 são: {inter_inic}")

tol = int(input("Insira um valor para o expoente da tolerância:"))
tol = 10**tol
print(f"o valor da tolerância é: {tol}")

Max = int(input("Insira o valor máximo de interações: "))
print(f"o valor máximo de interações é: {Max}")

jac = Jacobi(matriz, b, inter_inic, tol, Max, grau_da_matriz)


print(jac)