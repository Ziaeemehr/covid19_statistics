import os
import lib
import numpy as np
import pylab as pl
import pandas as pd
from copy import copy
from os.path import join
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.gridspec as gridspec


cols = ['Date_reported',
        ' Country_code',
        ' Country',
        ' WHO_region',
        ' New_cases',
        ' Cumulative_cases',
        ' New_deaths',
        ' Cumulative_deaths']

data_path = "../dataset"
file_name = "WHO-COVID-19-global-data.csv"
fontsize = 12
labelsize = 12


df = pd.read_csv(join(data_path, file_name))
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
# print(df.columns)
# exit(0)
countries = list(set(df[' Country']))
countries.sort()

# countries = ['Iran (Islamic Republic of)']

if 0:
    for i in range(len(countries)):

        filter_country = df[' Country'] == countries[i]
        sample_data = df[filter_country]

        fig, ax = pl.subplots(nrows=2, ncols=2,
                              figsize=(12, 7), sharex=True)

        x = sample_data['Date_reported']
        labels = [[' New_cases', ' Cumulative_cases'],
                  [' New_deaths', ' Cumulative_deaths']]
        for row in range(2):
            for col in range(2):
                y = sample_data[labels[row][col]]
                ax[row][col].bar(x, y, color='gray')
                date_form = DateFormatter("%m-%d")
                ax[row][col].xaxis.set_major_formatter(date_form)
                ax[row][col].set_xlabel("Date", fontsize=fontsize)
                ax[row][col].set_ylabel(labels[row][col], fontsize=fontsize)
                ax[row][col].tick_params(labelsize=labelsize)
                pl.setp(ax[row][col].xaxis.get_majorticklabels(), rotation=70)
                if (row == col == 0):
                    ax[row][col].set_title(countries[i])

        pl.tight_layout()
        pl.savefig(join("../data", "fig", countries[i]+".png"))
        pl.close()


# fig, ax = pl.subplots(2, figsize=(6, 5))
fig = pl.figure(figsize=(8, 12))
outer = gridspec.GridSpec(3, 2, wspace=0.2, hspace=0.2)


def plot_(country, outer, jj=0, labelsize=14):

    inner = gridspec.GridSpecFromSubplotSpec(2, 1,
                                             subplot_spec=outer, wspace=0.1, hspace=0.1)
    ax = []
    for i in range(2):
        ax.append(pl.Subplot(fig, inner[i]))
        fig.add_subplot(ax[-1])

    filter_country = df[' Country'] == country
    sample_data = df[filter_country]
    x = sample_data['Date_reported']
    labels = [' New_cases', ' New_deaths']
    legend_labels = ['new cases', 'new death']

    new_case = sample_data[labels[0]]
    new_death = sample_data[labels[1]]

    ax[0].bar(x, new_case, color='gray')
    ax[1].bar(x, new_death, color='red')
    date_form = DateFormatter("%m-%d")
    for i in range(2):
        ax[i].xaxis.set_major_formatter(date_form)
        ax[i].set_ylabel(legend_labels[i], fontsize=fontsize)
        ax[i].tick_params(labelsize=labelsize)
        
        if (jj==4) or (jj==5):
            pl.setp(ax[i].xaxis.get_majorticklabels(), rotation=70)
        else:
            ax[i].set_xticks([])
    
    ax[0].set_xticks([])
    ax[0].text(0.05, 0.85, country, fontsize=12, transform=ax[0].transAxes)
    ax[1].set_xlabel("Date", fontsize=fontsize)


countries = ['Iran (Islamic Republic of)',
             'Turkey',
             'Italy',
             'Spain',
             'The United Kingdom',
             'United States of America'
             ]
for i in range(6):
    plot_(countries[i], outer[i], jj=i)

pl.show()


# pl.xticks(rotation=70)
# index_date = copy(sample_data['Date_reported'])
# index_date = [pd.to_datetime(date, format='%Y-%m-%d').date()
#         for date in index_date]
# sample_data.plot.bar(x='Date_reported', y='New_cases', ax=ax, label="Iran")
# ax.xaxis.set_major_locator(mdates.DateFormatter('%d-%m-%Y'))
# print(type(countries), type(countries[0]), len(countries))
# print(type(df['Date_reported'][0]))
# print(type(df['Date_reported'][0]))
# print(df.head())
# print(df.columns)
# print(df)
# print(sample_data)
