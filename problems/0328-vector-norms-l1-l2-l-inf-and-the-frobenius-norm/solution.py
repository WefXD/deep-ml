import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == "l1":
        return float(sum(abs(num) for num in arr.flatten()))
    elif norm_type == "l2":
        return float(sum(num**2 for num in arr.flatten())**.5)
    elif norm_type == "linf":
        return float(max(abs(num) for num in arr.flatten()))
    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("frobenius norm must be done on 2d matrix")
        return float(sum(num**2 for num in arr.flatten())**.5)
    
    else:
        raise ValueError(f"{norm_type} is not an accetable norm_type")

