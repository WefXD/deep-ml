import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	x = np.zeros_like(b)
	for i in range(len(A)):

		pivot = np.argmax(np.abs(A[i:, i])) + i

		A[[i, pivot]] = A[[pivot, i]]
		b[[i, pivot]] = b[[pivot, i]]

		for j in range(i+1, len(A)):
			r = A[j][i] / A[i][i]
			A[j] -= A[i]*r
			b[j] -= b[i]*r

	for i in range(len(A)-1, -1, -1):
		goal = b[i]
		for j in range(len(A)-1,i,-1):
			b[i] -= A[i][j] * x[j]
		x[i] = b[i]/A[i][i]
		
	
	return x
