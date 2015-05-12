'''
Filename: CalcForecastStat.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: Takes the Survey of Professional Forecasters (SPF) forecasts 
and calculates the 4 quarter ahead CPI, GDP and unemployment rates.
'''
from LoadRawData import loadxlsdata
import pandas as pd
import numpy as np


def CalcForecastStats():
    '''Load the SPF raw data and calcuate the necessary statistics '''
    try:
        'Load Data'
        CPIforecast = loadxlsdata('Median_CPI_Level.xls')
        GDPforecast = loadxlsdata('Median_RGDP_Level.xls')
        Unemploymentrateforecast = loadxlsdata('Median_UNEMP_Level.xls')

        'Drop any unnecessary columns'
        CPIforecast.drop(['YEAR', 'QUARTER', 'CPI1', 'CPI2', 'CPI3', 'CPI4', 'CPI5', 'CPIA', 'CPIB', 'CPIC'], axis=1, inplace = True)
        Unemploymentrateforecast.drop(['YEAR', 'QUARTER', 'UNEMP1', 'UNEMP2', 'UNEMP3', 'UNEMP4', 'UNEMP5', 'UNEMPA', 'UNEMPB', 'UNEMPC', 'UNEMPD'], axis=1, inplace = True)

        'Calculate the year-over-year GDP growth rate'
        GDP4qtrforecast = np.log(GDPforecast.RGDP6/GDPforecast.RGDP2)*100
        GDP4qtrforecast = pd.DataFrame(GDP4qtrforecast, columns=['GDP4qtrforecast'])

        'Drop any unnecessary columns'
        GDP4qtrforecastforoutput = pd.merge(GDPforecast, GDP4qtrforecast, left_index = True, right_index = True)
        GDP4qtrforecastforoutput.drop(['YEAR', 'QUARTER', 'RGDP1', 'RGDP2', 'RGDP3', 'RGDP4', 'RGDP5', 'RGDP6','RGDPA', 'RGDPB', 'RGDPC', 'RGDPD'], axis=1, inplace = True)
        
        'Combine on the necessary columns'
        Forecastdataset = pd.merge(CPIforecast, Unemploymentrateforecast, on='Date')
        Forecastdataset = pd.merge(Forecastdataset, GDP4qtrforecastforoutput, on = 'Date')
        Forecastdataset.set_index('Date', inplace = True)
        Forecastdataset = np.round(Forecastdataset, decimals =2)
        return Forecastdataset
    except IOError:
        print 'One of the SPF Forecast xls files is missing or misspelled-Please Check user manual'
        raise
