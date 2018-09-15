import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('speed_rpm_revised.csv', encoding='utf-8').drop('Unnamed: 0', axis=1).set_index('trip_id')
x = [i for i in range(len(df.index))]
y_dict = {'speed.mean': 'mean of speed', 'speed.median': 'median of speed', 'speed.mode': 'mode of speed'}

for key, value in y_dict.items():
    plt.plot(x, df[key])
    plt.xlabel('trip id')
    plt.ylabel(value)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.savefig(value + '.png')
    plt.close()

