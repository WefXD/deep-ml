import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    def mode(data):
        counts = {}
        for x in data:
            counts[x] = counts.get(x, 0) + 1
        return max(counts, key=counts.get)

    return {
        "mean" : np.mean(data),
        "median" : np.median(data),
        "mode" : mode(data),
        "variance" : np.var(data),
        "standard_deviation" : np.std(data),
        "25th_percentile" : (q1:=np.percentile(data, 25)),
        "50th_percentile" : np.percentile(data, 50),
        "75th_percentile" : (q3:=np.percentile(data, 75)),
        "interquartile_range" : q3-q1
    }
