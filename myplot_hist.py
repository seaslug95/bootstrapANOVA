### Packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme(style='darkgrid')

### Script
# Load results
df = pd.read_csv(r'.\results\results.csv')

# Plot histogram of pvalue differences
pvdiff = df['pval ONEWAY'] - df['pval BOOTS']
sns.histplot(pvdiff, kde=True)
plt.axvline(x=0, linestyle='--', color='red', linewidth=1)
plt.axvline(x=pvdiff.mean(), color='black', linewidth=2)

plt.show()
