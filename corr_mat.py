from string import letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
pd.set_option('display.max_rows', 1000)

# Import data
d = pd.read_csv("all_wells_lim_20k.csv", low_memory=False)

# Compute the correlation matrix
corr = d.corr()
print corr

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.2, cbar_kws={"shrink": .5}, ax=ax)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
sns.plt.show()