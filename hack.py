#! /usr/bin/env python3
# coding: utf-8
import pandas as pd
import numpy as np

data_list = []
for i in range(500+1):
    df = pd.read_csv('brightbox/chunk' + str(i) + '.csv', encoding='utf-8')
    df = df.loc[df.groupby('user_id')['speed'].idxmax()].drop('Unnamed: 0', axis=1)
    print('Iteration: ' + str(i))
    data_list.append(df)

res = pd.concat(data_list)
res.loc[res.groupby('user_id')['speed'].idxmax()].to_csv('res.csv')
