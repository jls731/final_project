'''
Filename: GetStatByDate.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: This function grabs the data from closest previous release date 
to the FOMC meeting date. This is for the economic statistics and forecasts.
'''

from datetime import datetime
from LoadEconStatDates import *

def GetEconStatByDate(dataset, releasedateunemploy, releasedateCPI, releasedatePCE, date):
    '''Retrieve CPI, PCE, core CPI, core PCE and unemployment rate data from the closest FOMC meeting date'''
    
    'Function to take input date and turn into datetime format'
    getdate = lambda s: datetime.strptime(s, "%Y/%m/%d")
    basedate = getdate(date)
    
    'load data'
    econstats = dataset

    'Find the closest date realized compared to the FOMC meeting date'
    rowreleasedateunemploy = releasedateunemploy.index.searchsorted(basedate)
    referencedateunemploy = releasedateunemploy.ix[releasedateunemploy.index[rowreleasedateunemploy-1]]

    rowreleasedateCPI = releasedateCPI.index.searchsorted(basedate)
    referencedateCPI = releasedateCPI.ix[releasedateCPI.index[rowreleasedateCPI-1]]
    
    rowreleasedatePCE = releasedatePCE.index.searchsorted(basedate)
    referencedatePCE = releasedatePCE.ix[releasedatePCE.index[rowreleasedatePCE-1]]    
    
    'Retrieve the data at that period'
    unemploymentrate = econstats.ix[referencedateunemploy]['UnemploymentRate']
    headlineCPI = econstats.ix[referencedateCPI]['CPIAUCNS']
    coreCPI = econstats.ix[referencedateCPI]['CPILFENS']
    headlinePCE = econstats.ix[referencedatePCE]['PCEPI']
    corePCE = econstats.ix[referencedatePCE]['PCEPILFE']
    return unemploymentrate, headlineCPI, coreCPI, headlinePCE, corePCE, referencedateunemploy, referencedateCPI, referencedatePCE

def GetGDPDataByDate(dataset, date):
    '''Retrieve the latest GDP data from the FOMC meeting date'''

    'Function to take input date and turn into datetime format'    
    getdate = lambda s: datetime.strptime(s, "%Y/%m/%d")
    basedate = getdate(date)
    
    'Find the row that is the closest to the FOMC meeting date'
    rowreleasedateGDP = dataset.index.searchsorted(basedate)
    referencedateGDP = dataset.ix[dataset.index[rowreleasedateGDP-1]]
    
    'Extract the data'
    GDP = referencedateGDP['GDP']
    year = referencedateGDP['Year']
    quarter = referencedateGDP['Quarter']
    return GDP, year, quarter
    
def GetFOMCDataByDate(dataset, date):
    '''For Each FOMC date, retrieve the Federal Funds Rate and any change from prior meeting'''

    'Function to take input date and turn into datetime format'    
    getdate = lambda s: datetime.strptime(s, "%Y/%m/%d")
    basedate = getdate(date)
    
    'Find the row that is the closest to the FOMC meeting date'
    rowreleasedateFOMC = dataset.index.searchsorted(basedate)
    referencedateFOMC = dataset.ix[dataset.index[rowreleasedateFOMC]]
    
    'Extract the data'
    Date = basedate
    FedFunds = referencedateFOMC['FedFunds']
    ChangeinFedFunds = referencedateFOMC['Change']
    return Date, FedFunds,ChangeinFedFunds

def GetForecastDataByDate(dataset, date):
    '''Retrieve the 1 year ahead CPI (year-over-year), unemployment rate, and GDP forecasts'''
    
    forecastdata = dataset
    
    'Function to take input date and turn into datetime format'    
    getdate = lambda s: datetime.strptime(s, "%Y/%m/%d")
    basedate = getdate(date)
   
    'Find the row that is the closest to the FOMC meeting date' 
    rowreleasedateforecast = forecastdata.index.searchsorted(basedate)
    referencedateforecast = forecastdata.ix[forecastdata.index[rowreleasedateforecast]]

    'Extract the data'
    CPIforecast = referencedateforecast['CPI6']
    unemploymentrateforecast = referencedateforecast['UNEMP6']
    GDPforecast = referencedateforecast['GDP4qtrforecast']
    return CPIforecast, unemploymentrateforecast, GDPforecast    


