'''
Filename: CalcEconStat.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: Takes the raw data from FRED and calculates the unemployment rate
and the year-over-year headline and core inflation rates
'''

from LoadRawData import loadfreddata
import urllib2
import pandas as pd
import numpy as np

def CalcEconStats():
    '''Calculates the inflation rate and unemployment rate statistics'''
    try:
        unemployeddata = loadfreddata(["UNEMPLOY","CLF16OV"])
        headlineCPI = loadfreddata("CPIAUCNS")
        coreCPI = loadfreddata("CPILFENS")
        headlinePCE = loadfreddata("PCEPI")
        corePCE = loadfreddata("PCEPILFE")
        
        'Estimate the unemployment rate and create series'
        unemploymentRate = 100*(unemployeddata.UNEMPLOY/unemployeddata.CLF16OV)
        unemploymentRate = unemploymentRate.map('{:,.2f}'.format)
        unemploymentRate = pd.DataFrame(unemploymentRate, columns=['UnemploymentRate'])
        unemploymentRate.reset_index(inplace=True)
    
        'Estimate the year-over-year % change for CPI and create DataFrame'
        headlineCPI_yoy = 100*(headlineCPI.pct_change(12))
        headlineCPI_yoy = np.round(headlineCPI_yoy, decimals=2)
        headlineCPI_yoy.reset_index(inplace=True)
    
        'Estimate the year-over-year % change for core CPI and create DataFrame'
        coreCPI_yoy = 100*(coreCPI.pct_change(12))
        coreCPI_yoy = np.round(coreCPI_yoy, decimals=2)
        coreCPI_yoy.reset_index(inplace=True)
    
        'Estimate the year-over-year % change for PCE deflator and create DataFrame'
        headlinePCE_yoy = 100*(headlinePCE.pct_change(12))
        headlinePCE_yoy = np.round(headlinePCE_yoy, decimals = 2)
        headlinePCE_yoy.reset_index(inplace=True)
    
        'Estimate the year-over-year % change for core PCE deflator and create DataFrame'
        corePCE_yoy = 100*(corePCE.pct_change(12))
        corePCE_yoy = np.round(corePCE_yoy, decimals =2)
        corePCE_yoy.reset_index(inplace=True)

        'Merge all the data together into one DataFrame'
        EconDataset = pd.merge(headlineCPI_yoy, coreCPI_yoy, on='DATE')
        EconDataset = pd.merge(EconDataset, headlinePCE_yoy, on='DATE')
        EconDataset = pd.merge(EconDataset, corePCE_yoy, on='DATE')
        EconDataset = pd.merge(EconDataset, unemploymentRate, on = 'DATE')
        EconDataset = EconDataset.drop(EconDataset.index[:12])
        EconDataset.set_index('DATE', inplace=True)
        return EconDataset
    
    except urllib2.URLError:
        raise

