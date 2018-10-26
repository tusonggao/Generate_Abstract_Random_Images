#数据来源；https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

df = df.sort_values('Date')
df.head()

#数据可视化
plt.figure(figsize=(18,9))
plt.plot(range(df.shape[0], (df['Low']+df['High'])/2.0))
plt.xticks(range(0, df.shape[0], 500), df['Date'].loc[::500], rotation=45)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Mid Price', fontsize=18)
plt.show()

high_prices = df.loc[:, 'High'].as_matrix()
low_prices = df.loc[:, 'Low'].as_matrix()
mid_prices = (high_prices + low_prices)/2.0
