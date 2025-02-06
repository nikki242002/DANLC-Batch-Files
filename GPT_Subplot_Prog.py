import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=12, freq='ME'),
    'North': np.random.randint(100, 500, 12),
    'South': np.random.randint(100, 500, 12),
    'East': np.random.randint(100, 500, 12),
    'West': np.random.randint(100, 500, 12)
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

regions = ['North', 'South', 'East', 'West']

fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(12, 8), sharex=True, sharey=True)
axes = axes.flatten()

for i, region in enumerate(regions):
    axes[i].plot(df['Date'], df[region], marker='D', color='Green',linestyle='--', label=region)
    axes[i].set_title(f'Sales in {region} Region')
    axes[i].set_xlabel('Date')
    axes[i].set_ylabel('Sales')
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.show()
