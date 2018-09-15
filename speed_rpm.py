#! /usr/bin/env python3
# coding: utf-8
import pandas as pd
import numpy as np
from scipy import stats

data_list = []
mode = lambda x: x.mode()
for i in range(500+1):
    df = pd.read_csv('brightbox/chunk' + str(i) + '.csv', encoding='utf-8')
    mask = (df['engine_rpm00'] > 0) & (df['speed'] > 0) & (df['speed'] < 300) & (df['mileage'] > 0) & (df['age'] > 15) & (df['duration'] > 0)
    df = df[mask].drop(['Unnamed: 0', 'engine_rpm'], axis=1)
    df = df.groupby('trip_id').agg({'speed': ['max', 'min', 'mean', 'median', lambda x: stats.mode(x)[0], 'std'], 'engine_rpm00': ['max', 'min', 'mean', 'median']})
    data_list.append(df)
    print('Iteration: ' + str(i))
res = pd.concat(data_list)
res = res.rename(columns={'<lambda>': 'mode'})
res = res.loc[res.index.drop_duplicates(keep=False)]
res.to_csv('speed_rpm.csv')
