import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot(typ, color='b'):
    """
    Possible values for typ:
    'acceleration',
    'deceleration'
    """
    df = pd.read_csv(typ + '_loc.csv', encoding='utf-8')
    x = df['latitude']
    y = df['longitude']

    plt.scatter(x, y, c=color)
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.title(typ + '-loc')
    plt.xlim(xmin=-90, xmax=90)
    plt.ylim(ymin=-180, ymax=180)
    plt.savefig(typ + '_loc.png')
    plt.show()
    plt.close()

scatter_plot('acceleration')
scatter_plot('deceleration', 'r')
