import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_table('/Users/vineethjason/Documents/University_of_Michigan/Winter_2020/EAS_639_006/PythonB/pythonB_assignments/weatherData/PTIM4/ptim4h2005.txt', delim_whitespace=True, names=("YYYY","MM","DD","hh","mm","WD","WSPD","GST","WVHT","DPD","APD","MWD","BAR","ATMP","WTMP","DEWP","VIS","TIDE"), low_memory=False)
df["dateTime"] = df["YYYY"].astype(str) + df["MM"].astype(str) + df["DD"].astype(str) + df["hh"].astype(str) + df["mm"].astype(str)

dfList = df['dateTime'][1:].tolist()
dateList = []
for d in dfList:
    dates = datetime.strptime(d, '%Y%m%d%H%M')
    dateList.append(dates)

a = ["YYYYMMDDhhmm"]
dateListnew = a + dateList
df["dateTimeTrue"] = dateListnew

df['ATMP'][1:] = df['ATMP'][1:].astype(float)

print(type(df['ATMP'][1]))

dfNew = df.loc[1:, ["dateTimeTrue", "ATMP"]]
#print(dfNew.head())
df[["ATMP"][1:]].plot()