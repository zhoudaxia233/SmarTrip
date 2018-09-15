import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('acceleration_loc.csv', encoding='utf-8')
df2 = pd.read_csv('deceleration_loc.csv', encoding='utf-8')

x1 = df1['latitude']
y1 = df1['longitude']
x2 = df2['latitude']
y2 = df2['longitude']

plt.scatter(x1, y1, c='b')
plt.scatter(x2, y2, c='r')

plt.xlabel('latitude')
plt.ylabel('longitude')
plt.xlim(xmin=-90, xmax=90)
plt.ylim(ymin=-180, ymax=180)
plt.show()
