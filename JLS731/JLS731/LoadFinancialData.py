'''
Filename: LoadFinancialData.py
Created by: Joseph Song
Last version on: 5/11/2015
Description: Load the daily financial data and merge to one dataframe
'''
from LoadRawData import loadcsvdata
import pandas as pd

def LoadFinancialData():
    '''Loads the financial data csvs and merges them into one dataframe'''
    
    try:
        'Load Spot Dollar Index, S&P 500 composite, 2-yr, 5-yr, 10-yr, and 30-yr Treasury yields'
        DXY = loadcsvdata('DXY.csv', ['Date'])
        SP500 = loadcsvdata('SP500.csv', ['Date'])
        TSY2 = loadcsvdata('TSY2YR.csv', ['Date'])
        TSY5 = loadcsvdata('TSY5YR.csv', ['Date'])
        TSY10 = loadcsvdata('TSY10YR.csv', ['Date'])
        TSY30 = loadcsvdata('TSY30YR.csv', ['Date']) 
    
        'Merge into one dataframe'
        financialdata = pd.merge(DXY, SP500, on='Date', how='outer')
        financialdata = pd.merge(financialdata, TSY2, on='Date', how = 'outer')
        financialdata = pd.merge(financialdata, TSY5, on='Date', how = 'outer')
        financialdata = pd.merge(financialdata, TSY10, on='Date', how = 'outer')
        financialdata = pd.merge(financialdata, TSY30, on='Date', how = 'outer')
        financialdata.set_index('Date', inplace = True)
        return financialdata
    except IOError:
        print 'One of the financial data files is missing or misspelled'
        raise
