import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    train_data = X_train.astype(float)
    test_data = X_test.astype(float)

    train_mean = np.mean(train_data, axis = 0)
    test_data -= train_mean
    train_std = np.std(train_data, axis = 0, ddof = 0)
    train_std = np.where(train_std == 0, 1, train_std)
    test_data /= train_std
    return test_data
