#Lab2 Q3

import pandas as pd
datafile = pd.read_csv("weather_data.txt")


#print(data_file)
#print(df.info())
#print(df.columns)


#a) Day with highest precipitation
highes_act_prep = datafile.actual_precipitation.max()
print("\nThe date with highest 'actual precipitation' is :")
print(datafile.loc[datafile.actual_precipitation == highes_act_prep,"date"])

#b) Average max temp for July 2014
print("\nAverage actual_max_temp for July 2014:")
print(datafile.loc[0:30, ['actual_max_temp']].mean()) #Input from July only

#c)
print("\nDays with the record max temp:")
print(datafile.loc[datafile.actual_max_temp == datafile.record_max_temp, "date"])

#d)Total rain in Oct 2014
print("\nTotal rain in October 2014:")
total = datafile.loc[92:122, "actual_precipitation"] #Collect data from October only
total = total.sum()
print(total)

#e)Day/s with low_temp < 60 and max_temp > 90
print("\nDays with low temp below 60 and max temp > 90:")
dates = (datafile.actual_min_temp < 60) & (datafile.actual_max_temp > 90)
print(datafile.loc[dates,"date"])