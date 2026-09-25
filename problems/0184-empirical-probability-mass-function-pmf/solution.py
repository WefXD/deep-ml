def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    m = {}
    for sample in samples:
        m[sample] = m.get(sample, 0) + 1/len(samples)
    
    return [(key, m[key]) for key in sorted(m)]
    
