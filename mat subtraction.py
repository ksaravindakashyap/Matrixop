from numpy import *

matrix1 = []
matrix = []
matrix2 = []
r1 = int(input("row1"))
c1 = int(input("col1"))
r2 = int(input("row2"))
c2 = int(input("col2"))

if r1!=r2 and c1!=c2:
    print("matrix subtraction is not possible")
else:

    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(int(input("enter elements of first matrix")))
        matrix1.append(a)
    for i in range(r1):
        for j in range(c1):
            print(matrix1[i][j],end=" ")
        print()


    for i in range(r2):
        b = []
        for j in range(c2):
            b.append(int(input("enter elements of secound matrix")))
        matrix2.append(b)
    for i in range(r2):
        for j in range(c2):
            print(matrix2[i][j],end=" ")
        print()


    print("the final matrix")
    for i in range(r2):
        d = []
        for j in range(c2):
            d.append(0)
            matrix.append(d)
            matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            print(matrix[i][j],end=" ")
        print()

    if matrix[i][j]==0 :
        print("it is zero matrix")
    if matrix[i][j]==1 :
        print("matrix of ones")
