def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	ret = []
	if mode == "row":
		return [sum(row)/len(row) for row in matrix]
	return [
		sum(matrix[row][col] for row in range(len(matrix)))/len(matrix) for col in range(len(matrix[0]))
	]