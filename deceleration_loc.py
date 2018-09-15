import pandas as pd

data_list = []
for i in range(500+1):
    df = pd.read_csv('brightbox/chunk' + str(i) + '.csv', encoding='utf-8')
    mask = (df['engine_rpm00'] > 0) & (df['speed'] > 0) & (df['speed'] < 300) & (df['mileage'] > 0) & (df['age'] > 15) & (df['duration'] > 0)
    df = df[mask].drop(['Unnamed: 0', 'engine_rpm'], axis=1)
    df = df[df['decelerations_count'].diff() == 1]
    df = df[['latitude', 'longitude']]
    data_list.append(df)
    print('Iteration: ' + str(i))
res = pd.concat(data_list).reset_index(drop=True)
res.to_csv('deceleration_loc.csv')
