### Packages
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mymodule
sns.set_theme(style='darkgrid')

### Script
# Load results
df = pd.read_csv(r'.\results\results.csv')

# Fit a linear regression model
slope, intercept, r_value, p_value, std_err = stats.linregress(x=df['pval ONEWAY'], y=df['pval BOOTS'])

# Create a regression plot + add marginal distributions (histograms) and the identity line
sns.jointplot(x='pval ONEWAY', y='pval BOOTS', data=df, kind='reg', ci=None, marginal_kws={'bins': np.arange(0, 1.00000001, 0.05)})
sns.lineplot(x='pval ONEWAY', y='pval ONEWAY', data=df, linestyle='--', color='red', linewidth=1)

# Add the R-squared and p-value to the plot
text = f'R2 : {r_value**2:.3f}\npval : {mymodule.fpval(p_value)}'
plt.text(0.6, 0.2, text, transform=plt.gca().transAxes)

plt.show()
