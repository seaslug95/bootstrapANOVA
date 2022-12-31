### Packages
import itertools
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
sns.set_theme(style='darkgrid')

### Parameters
n_pval = 50
# np.random.seed(seed=1)

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

### Script
pval_ONEWAY = []
pval_BOOTS = []
for i in range(n_pval):
    # Generate 5 groups of samples
    mean1, sd1, size1 = 0, 1 + np.random.uniform(-0.5, 0.5), np.random.randint(50, 150)
    mean2, sd2, size2 = 0, 1 + np.random.uniform(-0.5, 0.5), np.random.randint(50, 150)
    mean3, sd3, size3 = 0, 1 + np.random.uniform(-0.5, 0.5), np.random.randint(50, 150)
    mean4, sd4, size4 = 0, 1 + np.random.uniform(-0.5, 0.5), np.random.randint(50, 150)
    mean5, sd5, size5 = 0, 1 + np.random.uniform(-0.5, 0.5), np.random.randint(50, 150)
    sample1 = list(np.random.normal(loc=mean1, scale=sd1, size=size1))
    sample2 = list(np.random.normal(loc=mean2, scale=sd2, size=size2))
    sample3 = list(np.random.normal(loc=mean3, scale=sd3, size=size3))
    sample4 = list(np.random.normal(loc=mean4, scale=sd4, size=size4))
    sample5 = list(np.random.normal(loc=mean5, scale=sd5, size=size5))
    samples = [sample1, sample2, sample3, sample4, sample5]

    # Compute bootstrapped and oneway ANOVA p values
    pvalue_boots = pvalBootAnova(samples=samples)
    pval_BOOTS.append(pvalue_boots)
    ttest, pvalue_anova = stats.f_oneway(sample1, sample2, sample3, sample4, sample5)
    pval_ONEWAY.append(pvalue_anova)
    
data = pd.DataFrame({'pval ONEWAY': pval_ONEWAY, 'pval BOOTS': pval_BOOTS})

# Fit a linear regression model
slope, intercept, r_value, p_value, std_err = stats.linregress(x=np.array(pval_ONEWAY), y=np.array(pval_BOOTS))

# Create a regression plot using seaborn
sns.regplot(x='pval ONEWAY', y='pval BOOTS', data=data, ci=None)
sns.jointplot(x='pval ONEWAY', y='pval BOOTS', data=data, kind='reg', ci=None, marginal_kws={'bins': np.arange(0, 1.00000001, 0.05)})
sns.lineplot(x='pval ONEWAY', y='pval ONEWAY', data=data, linestyle='--', color='red', linewidth=1)

# Add the R-squared and p-value to the plot
text = f'R2 : {r_value**2:.3f}\npval : {fpval(p_value)}'
plt.text(0.6, 0.2, text, transform=plt.gca().transAxes)

# Show the plot
plt.show()
