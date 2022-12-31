### Packages
import itertools
import numpy as np
import math

### Functions
def fpval(pval:float) -> str:
    """Returns formatted pvalue"""
    magnitude = int(math.floor(math.log10(pval)))
    mantissa = pval / 10**magnitude
    res = f"{mantissa:.2f}E{magnitude}"
    return res

def sumSquares(sample:list) -> float:
    """Returns sum of squared differences from sample mean"""
    res = np.array(sample).var() * len(sample)
    return res

def fBootAnova(samples:list) -> float:
    """Returns custom F stat (ANOVA) from list of samples"""
    concSamples = list(itertools.chain(*samples))
    ssto = sumSquares(concSamples)
    sst = 0
    for s in samples:
        s_mean = np.array(s).mean()
        s_n = len(s)
        sst = sst + s_n * s_mean**2
    sst = sst - len(concSamples) * np.array(concSamples).mean()**2
    f_stat = sst / (ssto - sst)
    return f_stat

def pvalBootAnova(samples:list, num_samples=10000):
    """Returns pvalue from bootstrapped ANOVA"""
    original_fstat = fBootAnova(samples=samples)
    concSamples = list(itertools.chain(*samples))
    boot_fstats = []
    for i in range(num_samples):
        new_samples = list()
        for j in range(len(samples)):
            new_sample = np.random.choice(concSamples, size=len(samples[j]), replace=True)
            new_samples.append(list(new_sample))
        # new_samples = np.array(new_samples)
        boot_fstat = fBootAnova(new_samples)
        boot_fstats.append(boot_fstat)
    p_value = np.sum(np.abs(boot_fstats) >= np.abs(original_fstat)) / len(boot_fstats)
    return p_value
