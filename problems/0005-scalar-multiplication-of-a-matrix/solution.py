def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	ret = []
	for row in matrix:
		ret.append([item * scalar for item in row])
	return ret