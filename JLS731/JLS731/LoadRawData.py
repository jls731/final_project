'''
Created by: Joseph Song
Last version on: 5/11/2015
Description: Has the functions needed to load csv, xls, and FRED data.
'''

import pandas.io.data as web
import pandas as pd
import datetime


def loadfreddata(ticker):
    '''Loads the FRED Data from the St. Louis Fed Website as a dataframe'''
    start = datetime.datetime(1998,12,1)
    end = datetime.datetime(2015,3,1)
    data = web.DataReader(ticker, "fred", start, end)
    return data

def loadcsvdata(filename, datecol):
    '''Loads the CSV Data as a dataframe'''
    parsedate = lambda x: pd.to_datetime(x)
    dataset = pd.read_csv(filename, parse_dates = datecol, date_parser = parsedate)
    return dataset

def loadxlsdata(filename):
    '''Loads the excel files as a dataframe'''
    data = pd.read_excel(filename, sheetname = 0)
    return data


'''
import urllib2
import numpy as np

x = loadcsvdata('NFP.csv', ['Date', 'NFP_Release'])
print x

x = loadcsvdata('NF.csv', ['Date', 'NFP_Release'])
print x.info()
print x


'''
        