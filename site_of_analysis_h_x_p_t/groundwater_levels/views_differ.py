from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
#ONLY SIMPLE COMMENTS in order to have execi
def diplay_xls(request):
#%%
#!!!!!!!
# Simple comments in order to illustrate a procedure of COMMIT
#!!!!!!!
# set the path to the file
#    xse with COMMITls_path = settings.BASE_DIR / 'static'
    xls_path = settings.BASE_DIR / 'static'
# make an empty list for dataframes
    dfs = []
# create dataframs, store as list
    for i in range(0, 4):
        df = pd.read_excel(xls_path / 'wl_table.xlsx', sheet_name = i)
        dfs.append(df)

# output below - dataframe with all data
        dataframe = pd.concat(dfs)
    print(dataframe)
#%%

    p = dataframe["Давление, мм рт. ст."]  #dataframe.values[:, 1::].astype('float')
    h = dataframe["Уровень грунтовых вод, см"]
    x = dataframe["Осадки, мм"]
    t = dataframe["Температура, гр.С"]
    dates = dataframe["Дата"]
    #corrs = dataframe.corr(numeric_only=True)

#%%

# matplotlib understands dates from pandas
# plot simple graphs

    #plt.figure(dpi = 256)
    #plt.plot(dates, values)#[:,0])
    #plt.grid()
    #plt.xticks(ha = 'right', rotation = 30)

    fig = plt.figure(dpi = 256)
    ax = fig.add_subplot(projection='3d')
    ax.scatter(p, x, t, marker='o', s=1)  # 3Д
    #ax.scatter(p, x, h, marker='o', s=1)
    #plt.plot(dates, values[:,4], marker = 'o', markersize = 3)

    # По очереди добавляем линии
    #plt.plot(dates, p, marker = 'o', markersize = 3)
    #plt.plot(dates, h, marker = 'o', markersize = 3)
    #plt.plot(dates, t, marker = 'o', markersize = 3)
    #plt.plot(dates, x, marker = 'o', markersize = 3)
    #plt.plot(p, t, marker = 'o', markersize = 3)
    #plt.grid()
    plt.xticks(ha = 'right', rotation = 30)

    img_name = 'graphname.png'
    img_path = settings.BASE_DIR / 'static' / img_name
    plt.savefig(img_path)
    return render(
        request,
        'groundwater_levels/index.html',
        {
            'plotsrc': img_name  # работать не будет!
        }
    )



