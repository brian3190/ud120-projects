def featureScaling(arr):
    nmax = max(data)
    nmin = min(data)
    if (nmax == nmin):
        return None
    rang = nmax - nmin
    return [float(e-nmin)/rang for e in data ]


data = [115, 140, 175]
print featureScaling(data)
