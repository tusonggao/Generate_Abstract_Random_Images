#数据来源；https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.preprocessing import MinMaxScaler

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

train_data = mid_prices[:11000]
test_data = mid_prices[11000:]

scaler = MinMaxScaler()
train_data = train_data.reshape(-1, 1)
test_data = test_data.reshape(-1, 1)

smoothing_window_size = 2500
for di in range(0, 10000, smoothing_window_size):
    scaler.fit(train_data[di:di+smoothing_window_size, :])
    train_data[di:di+smoothing_window_size, :] = scaler.transform(
        train_data[di:di+smoothing_window_size, :])


scaler.fit(train_data[di+smoothing_window_size, :])
train_data[di+smoothing_window_size, :] = scaler.transform(
    train_data[di+smoothing_window_size, :])

train_data = train_data.reshape(-1)
test_data = scaler.transform(test_data).reshape(-1)

EMA = 0.0
gamma = 0.1
for ti in range(11000):
    EMA = gamma + train_data[ti] + (1-gamma)*EMA
    train_data[ti] = EMA

all_mid_date = np.concatenate([train_data, test_data], axis=0)

window_size = 100
N = train_data.size

run_avg_predictions = []
run_avg_x = []
mse_errors = []
running_mean = 0.0
run_avg_predictions.append(running_mean)
decay = 0.5

for pred_idx in range(1, N):
    running_mean = running_mean*decay + (1.0-decay)*train_data[pred_idx-1]
    run_avg_predictions.append(running_mean)
    mse_errors.append((run_avg_predictions[-1]-train_data[pred_idx])**2)
    run_avg_x.append(date)

print('MSE error for EMA averaging: %.5f'%(0.5*np.mean(mse_errors)))