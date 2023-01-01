### Packages
import itertools
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
import mymodule

### Parameters
n_pval = 100

np.random.seed(seed=1) # Reproducibility

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
    pvalue_boots = mymodule.pvalBootAnova(samples=samples)
    pval_BOOTS.append(pvalue_boots)
    ttest, pvalue_anova = stats.f_oneway(sample1, sample2, sample3, sample4, sample5)
    pval_ONEWAY.append(pvalue_anova)
    
df = pd.DataFrame({'pval ONEWAY': pval_ONEWAY, 'pval BOOTS': pval_BOOTS})
df.to_csv(r'.\results\results.csv', index=False, header=True)
