def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	def determinant(matrix):
		n = len(matrix)
		if n == 1:
			return matrix[0][0]
		det = 0
		for col in range(n):
			minor = [
				row[:col] + row[col + 1:] for row in matrix[1:]
			]
			det += ((-1) ** col) * matrix[0][col] * determinant(minor)
		return det
		
	trace = sum(matrix[i][i] for i in range(len(matrix)))

	return (float(determinant(matrix)), float(trace))