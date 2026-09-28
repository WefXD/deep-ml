import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	data = data.astype(float)
	# Your code here
	standardized_data = data-np.mean(data, axis = 0)
	standardized_data /= np.std(data, axis = 0)

	normalized_data = data-np.min(data, axis = 0)
	normalized_data /= np.max(normalized_data, axis = 0)


	return standardized_data, normalized_data