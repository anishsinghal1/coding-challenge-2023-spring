
import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv('6 class csv.csv')
file['Temperature (K)'].plot(kind='hist', edgecolor = 'black', bins = 10)
plt.title('Distribution of Temperature (K) in star dataset')
plt.xlabel('Temperature (K)')
plt.show()
