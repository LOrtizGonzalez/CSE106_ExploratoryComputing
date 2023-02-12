#Lab2 Q4

import pandas as pd
import matplotlib.pyplot as plt

datafile = pd.read_csv("weather_data.txt")

#a)
#Put the values into Lists
minTemp = datafile.actual_min_temp
maxTemp = datafile.actual_max_temp
plt.plot(minTemp, color = "blue", label = "actual min temp")
plt.plot(maxTemp, color = "red", label = "actual max temp")
plt.xlabel("days")
plt.ylabel("temp")
plt.title("day/temp")
plt.legend()
plt.show()

#b)
histogram = datafile["actual_precipitation"].plot(kind = 'hist')
plt.xlabel("precip amount")
plt.ylabel("days")
plt.title("actual precipitation")
plt.show()