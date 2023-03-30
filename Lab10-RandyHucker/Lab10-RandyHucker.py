import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('dataset.csv',
                     header=None,
                     names=['Year', 'Title', 'Comic', 'IMDB', 'RT', '', 'OpeningWeekendBoxOffice', 'AvgTicketPriceThatYear', 'EstdOpeningAttendance', 'USPopThatYear'])

sh = sh_raw[np.isfinite(
    sh_raw.OpeningWeekendBoxOffice)]

# print(sh)

# print(sh.head(5))

# Normalize and scatterplot the scores
# imdb_normalized = sh.IMDB / 10
# sh.insert(10, 'IMDBNormalized', imdb_normalized)
# rt_normalized = sh.RT/100
# sh.insert(11, 'RTNormalized', rt_normalized)
# sh.plot.scatter(x='RTNormalized', y='IMDBNormalized')
# plt.show()

# print(sh[['RTNormalized','IMDBNormalized']].corr())
# print(sh[['RTNormalized','IMDBNormalized']].describe())

# Required Lab Question 1:


def DCSeries(Dataframe):
    DCComics = pd.DataFrame(Dataframe)
    print(DCComics[DCComics["Comic"] == "DC"])

# Required Lab Question 2:


def PrintTwoColumnsDC(Dataframe):
    DCComics = pd.DataFrame(Dataframe)
    print(DCComics[DCComics["Comic"] == "DC"][list({"Year", "Title"})])

# Required Lab Question 3:


def PrintTwoColumnsMarvel(Dataframe):
    MarvelComics = pd.DataFrame(Dataframe)
    print(MarvelComics[MarvelComics["Comic"] == "Marvel"]
          [list({"Year", "Title"})])

# Required Lab Question 4:


def ScatterPlot():
    sh.insert(10, 'AVGPrice', sh.AvgTicketPriceThatYear)
    sh.insert(11, 'Year(Price)', sh.Year)
    sh.plot.scatter(x='Year', y='AVGPrice')
    plt.show()

# Required Lab Question 5:


def PrintCorrelation():
    sh.insert(10, 'AVGPrice', sh.AvgTicketPriceThatYear)
    print(sh[['Year', 'AVGPrice']].corr())

# Required Lab Question 6:


def SummaryStatistics():
    sh.insert(10, 'OpeningWeekend', sh.OpeningWeekendBoxOffice)
    print(sh[['OpeningWeekend']].describe())


# DCSeries(sh)
# PrintTwoColumnsDC(sh)
# PrintTwoColumnsMarvel(sh)
# ScatterPlot()
# PrintCorrelation()
# SummaryStatistics()
