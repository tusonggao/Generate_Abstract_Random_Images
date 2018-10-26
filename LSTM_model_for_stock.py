#数据来源；https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

df = df.sort_values('Date')
df.head()