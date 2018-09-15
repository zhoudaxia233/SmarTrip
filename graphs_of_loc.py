import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('acceleration_loc.csv', encoding='utf-8')
x = df['latitude']
y = df['longitude']

plt.scatter(x, y, c='b')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.title('acceleration-loc')
plt.xlim(xmin=-90, xmax=90)
plt.ylim(ymin=-180, ymax=180)
plt.savefig('acceleration_loc.png')
plt.show()
plt.close()

df = pd.read_csv('deceleration_loc.csv', encoding='utf-8')
x = df['latitude']
y = df['longitude']

plt.scatter(x, y, c='r')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.title('deceleration-loc')
plt.xlim(xmin=-90, xmax=90)
plt.ylim(ymin=-180, ymax=180)
plt.savefig('deceleration_loc.png')
plt.show()
plt.close()
