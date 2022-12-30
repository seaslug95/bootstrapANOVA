# generate bootstrap annova
import itertools
import numpy as np
from scipy.stats import f_oneway

np.random.seed(seed=1)

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


mean1, sd1, size1 = 0, 1, 50
mean2, sd2, size2 = 0, 1, 100
mean3, sd3, size3 = 0, 1, 100
sample1 = list(np.random.normal(loc=mean1, scale=sd1, size=size1))
sample2 = list(np.random.normal(loc=mean2, scale=sd2, size=size2))
sample3 = list(np.random.normal(loc=mean3, scale=sd3, size=size3))
samples = [sample1, sample2, sample3]

pvalue_boot = pvalBootAnova(samples=samples)
print('pvalue_boots :',pvalue_boot)

ttest, pvalue_anova = f_oneway(sample1, sample2, sample3)
print('pvalue_anova :',pvalue_anova)
