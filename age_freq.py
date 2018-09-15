#! /usr/bin/env python3
# coding: utf-8
import pandas as pd

data_list = []
for i in range(500+1):
    df = pd.read_csv('brightbox/chunk' + str(i) + '.csv', encoding='utf-8')
    df = df.groupby('user_id').first()[['age']]
    print('Iteration: ' + str(i))
    data_list.append(df)
res = pd.concat(data_list)
res = res.reset_index().drop_duplicates('user_id').set_index('user_id')
res = res['age'].value_counts().to_frame()
res.to_csv("age_freq.csv")
