import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = len(data)
    indices = np.random.default_rng(seed).permutation(n)
    train_end = int(n*train_frac)
    validation_end = train_end + int(validation_frac*n)
    train = []
    validation = []
    test = []
    for i in range(train_end):
        j = indices[i]
        train.append(data[j])
    for i in range(train_end, validation_end):
        j = indices[i]
        validation.append(data[j])
    for i in range(validation_end, n):
        j = indices[i]
        test.append(data[j])
    return [np.array(train), np.array(validation), np.array(test)]
