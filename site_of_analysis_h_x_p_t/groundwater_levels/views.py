from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
def display_xls(request):
#%%
# set the path to the file
    xls_path = settings.BASE_DIR / 'static'
# make an empty list for dataframes
    dfs = []
# create dataframs, store as list
    for i in range(0, 4):
        df = pd.read_excel(xls_path / 'wl_table.xlsx', sheet_name = i)
        dfs.append(df)

# output below - dataframe with all data
        dataframe = pd.concat(dfs)

#%%

    values = dataframe.values[:, 1::].astype('float')
    dates = dataframe.Дата
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

def data_table(col='h'):
    data = read_xls(settings.BASE_DIR / 'static')
    print(data['d'][1])
    print(data[col][1])
    print(zip(data['d'][1], data['h'][1]))
    context = {
        'd': data['d'][0],
        'c': data[col][0],
        'dh': zip(data['d'][1], data[col][1])
    }
    return context


def groundwater_levels(request):
    context = data_table('h')
    return render(
        request,
        'groundwater_levels/datatable.html',
        context
    )

def pressure(request):
    context = data_table('p')
    return render(
        request,
        'groundwater_levels/datatable.html',
        context
    )

def precipitation(request):
    context = data_table('x')
    return render(
        request,
        'groundwater_levels/datatable.html',
        context
    )

def air_temperature(request):
    context = data_table('t')
    return render(
        request,
        'groundwater_levels/datatable.html',
        context
    )


def read_xls(xls_path, year=0):
# make an empty list for dataframes
    dfs = []
# create dataframs, store as list
    for i in range(0, 4):
        df = pd.read_excel(xls_path / 'wl_table.xlsx', sheet_name = i)
        dfs.append(df)

# output below - dataframe with all data
        dataframe = pd.concat(dfs)
    print(dataframe)
    if year:
        dataframe = dataframe[dataframe["Дата"].dt.year==year]
        print(year)
        print(dataframe)
    #df[df['Date'].dt.year == year]
#%%

    p = dataframe["Давление, мм рт. ст."]  #dataframe.values[:, 1::].astype('float')
    h = dataframe["Уровень грунтовых вод, см"]
    x = dataframe["Осадки, мм"]
    t = dataframe["Температура, гр.С"]
    dates = dataframe["Дата"]
    return {
        'd': ["Дата", dates],
        'p': ["Давление, мм рт. ст.", p],
        't': ["Температура, гр.С", t],
        'x': ["Осадки, мм", x],
        'h': ["Уровень грунтовых вод, см", h]

    }


def draw(request):
    context = {}
    if request.method == 'POST':
        print(request.POST['ax1'])
        ax1 = request.POST['ax1']
        print(request.POST['ax2'])
        ax2 = request.POST['ax2']
        year = request.POST['year']
        data = read_xls(settings.BASE_DIR / 'static', int(year))
        fig = plt.figure(dpi = 256)
        #ax = fig.add_subplot(projection='3d')
        #ax.scatter(p, x, t, marker='o', s=1)  # 3Д
        plt.title(data[ax2][0] + " от " + data[ax1][0])
        plt.xlabel(data[ax1][0])
        plt.ylabel(data[ax2][0])
        plt.plot(data[ax1][1], data[ax2][1], marker = 'o', markersize = 3)
    #plt.plot(dates, h, marker = 'o', markersize = 3)
    #plt.plot(dates, t, marker = 'o', markersize = 3)
    #plt.plot(dates, x, marker = 'o', markersize = 3)
    #plt.plot(p, t, marker = 'o', markersize = 3)
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.xticks(ha = 'right', rotation = 30)

        img_name = 'graphname.png'
        img_path = settings.BASE_DIR / 'static' / img_name
        plt.savefig(img_path)
        context = {
            'plotsrc': img_name 
        }

    return render(
        request,
        'groundwater_levels/analysis.html',
        context
    )

def show_links(request):
    return render(
        request,
        'groundwater_levels/neuronet.html'
    )

def show_pictures(request):
    return render(
        request,
        'groundwater_levels/neuronet_in_hydrological_forecasts.html'
    )


def show_graphics(request):
    return render(
        request,
        'groundwater_levels/lack_of_correlation.html'
    )

def hxpt(request):
    context = {}
    data = read_xls(settings.BASE_DIR / 'static')
    fig = plt.figure(dpi = 256)
    #ax = fig.add_subplot(projection='3d')
    #ax.scatter(p, x, t, marker='o', s=1)  # 3Д
    plt.title(data['h'][0] + " и " + data['x'][0])
    plt.xlabel(data['h'][0])
    plt.ylabel(data['x'][0])
    #
    #plt.legend([data['h'][0], data['x'][0]])
    plt.legend(['uuu', 'l;l'])
    
    plt.plot(
        data['d'][1],
        data['h'][1],
        marker = 'o',
        markersize = 3,
        label=data['h'][0],
        color='red')
    plt.plot(
        data['d'][1],
        data['x'][1],
        markersize = 1,
        color='green')
    
    #plt.plot(dates, t, marker = 'o', markersize = 3)
    #plt.plot(p, t, marker = 'o', markersize = 3)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.xticks(ha = 'right', rotation = 30)

    img_name = 'hxpt.png'
    img_path = settings.BASE_DIR / 'static' / img_name
    plt.savefig(img_path)
    context = {
        'plotsrc': img_name 
    }

    return render(
        request,
        'groundwater_levels/analysis.html',
        context
    )




