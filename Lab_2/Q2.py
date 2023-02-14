#Lab2 Q2
import numpy as np
#import decimal

#a)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix A:")
for row in A:
    print(row)
B = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])
print("\nMatrix B:")
for row in B:
    print(row)
C = A + B
print("\nMatrix C (sum of A and B):")
print(C)

#b)
D = A.dot(B)
print("The product of A and B:")
print(D)

#c)
d = np.linalg.det(A)
print("determinant of A:")
print(d) # trying to print to two decimal places

#d)
print("Inverse of B:\n", np.linalg.inv(B))

#e)
w,v = np.linalg.eig(A)
print("Eigen values of A:\n", w)