# -*- coding: utf-8 -*-
#%% loading libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os

#%%
# set the path to the file
path_to_file = os.sys.argv[1]

# make an empty list for dataframes
dfs = []

# create dataframs, store as list
for i in range(0, 4):
    df = pd.read_excel(path_to_file, sheet_name = i)
    dfs.append(df)

# output below - dataframe with all data
dataframe = pd.concat(dfs)

#%%

values = dataframe.values[:, 1::].astype('float')
print(dataframe)
dates = dataframe['Дата']
corrs = dataframe.corr(numeric_only=True)

#%%

# matplotlib understands dates from pandas
# plot simple graphs

plt.figure(dpi = 256)
plt.plot(dates, values[:,0])
plt.grid()
plt.xticks(ha = 'right', rotation = 30)

plt.figure(dpi = 256)
plt.plot(dates, values[:,4], marker = 'o', markersize = 3)
plt.grid()
plt.xticks(ha = 'right', rotation = 30)
plt.savefig('picture.png')
