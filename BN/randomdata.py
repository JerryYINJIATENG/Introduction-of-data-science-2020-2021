import numpy as np
import pandas as pd

values = pd.DataFrame(np.random.randint(low=0, high=1000, size=(1000, 6)), columns=['PT', 'BT', 'HO', 'SA', 'PX', 'HA'])
val = values.copy()
for index, row in val.iterrows():
    if row['PT'] <= 200:
        val['PT'][index] = 1
    else:
        val['PT'][index] = 0
    if row['BT'] <= 1:
        val['BT'][index] = 1
    else:
        val['BT'][index] = 0
for index, row in val.iterrows():
    if row['PT'] == 0:
        if np.random.random() < 1.0:
            val['HO'][index] = 0
        else:
            val['HO'][index] = 1
    else:
        if np.random.random() < 0.3:
            val['HO'][index] = 0
        else:
            val['HO'][index] = 1

for index, row in val.iterrows():
    if row['HO'] == 0:
        if np.random.random() < 0.9:
            val['SA'][index] = 0
        else:
            val['SA'][index] = 1
    else:
        if np.random.random() < 0.2:
            val['SA'][index] = 0
        else:
            val['SA'][index] = 1
for index, row in val.iterrows():
    if row['BT'] == 0:
        if np.random.random() < 0.9:
            val['PX'][index] = 0
        else:
            val['PX'][index] = 1
    else:
        if np.random.random() < 0.2:
            val['PX'][index] = 0
        else:
            val['PX'][index] = 1
for index, row in val.iterrows():
    if row['BT'] == 0 and row['HO'] == 0:
        if np.random.random() < 0.98:
            val['HA'][index] = 0
        else:
            val['HA'][index] = 1
    elif row['BT'] == 1 and row['HO'] == 0:
        if np.random.random() < 0.1:
            val['HA'][index] = 0
        else:
            val['HA'][index] = 1
    elif row['BT'] == 0 and row['HO'] == 1:
        if np.random.random() < 0.3:
            val['HA'][index] = 0
        else:
            val['HA'][index] = 1
    else:
        if np.random.random() < 0.01:
            val['HA'][index] = 0
        else:
            val['HA'][index] = 1
print(val)
val.to_csv('data.csv')
